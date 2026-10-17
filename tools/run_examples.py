#!/usr/bin/env python3
"""Виконує SQL-приклади з уроків і вставляє результати в Markdown.

Блок ```sql ... ```, після якого стоїть маркер <!-- run -->, виконується
на демо-базі DemoShop усередині транзакції, яка потім відкочується.
Результат вставляється між маркерами <!-- run:start --> і <!-- run:end -->
(повторний запуск оновлює результат).

Параметри маркера: <!-- run rows=20 --> — скільки рядків показати.

Режим --check перевіряє синтаксис (SET PARSEONLY) усіх інших блоків sql.

Потрібно: pip install pymssql, запущений SQL Server з базою DemoShop.
Змінні оточення: MSSQL_HOST, MSSQL_USER, MSSQL_PASSWORD.
"""
import datetime
import decimal
import html
import os
import re
import sys
from pathlib import Path

import pymssql

ROOT = Path(__file__).resolve().parent.parent
LESSONS = sorted((ROOT / "tutorial").glob("*.md"))

BLOCK_RE = re.compile(
    r"(```sql\n(?P<sql>(?:(?!```).)*?)\n```\n)"
    r"(?P<gap>\s*)"
    r"(?P<marker><!-- run:start(?P<opts2>[^>]*?)-->.*?<!-- run:end -->|<!-- run(?![:\w])(?P<opts>[^>]*?)-->)",
    re.S,
)
SQL_BLOCK_RE = re.compile(r"```sql\n(.*?)\n```", re.S)
GO_RE = re.compile(r"^\s*GO\s*$", re.M | re.I)


def connect(autocommit=False):
    conn = pymssql.connect(
        server=os.environ.get("MSSQL_HOST", "localhost"),
        user=os.environ.get("MSSQL_USER", "sa"),
        password=os.environ.get("MSSQL_PASSWORD", "Str0ng!Passw0rd"),
        database="DemoShop",
        autocommit=autocommit,
    )
    return conn


def fmt(value):
    if value is None:
        return '<span class="null">NULL</span>'
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, decimal.Decimal):
        return str(value)
    if isinstance(value, datetime.datetime):
        s = value.isoformat(sep=" ", timespec="milliseconds")
        return html.escape(s)
    if isinstance(value, (bytes, bytearray)):
        return "0x" + value.hex().upper()
    return html.escape(str(value), quote=False)


def render_table(columns, rows, max_rows):
    out = ['<div class="table-scroll"><table>']
    out.append("<tr>" + "".join(f"<th>{html.escape(c or '(Без назви)')}</th>" for c in columns) + "</tr>")
    for row in rows[:max_rows]:
        out.append("<tr>" + "".join(f"<td>{fmt(v)}</td>" for v in row) + "</tr>")
    out.append("</table></div>")
    if len(rows) > max_rows:
        out.append(f'<p class="result-more">… показано {max_rows} з {len(rows)} рядків</p>')
    else:
        out.append(f'<p class="result-more">Рядків: {len(rows)}</p>')
    return "\n".join(out)


def reseed(conn):
    """Відкат транзакції не повертає лічильники IDENTITY — повертаємо їх до максимального ключа."""
    cur = conn.cursor()
    cur.execute(
        "SELECT s.name, t.name, c.name, CAST(ic.seed_value AS BIGINT) "
        "FROM sys.identity_columns ic "
        "JOIN sys.tables t ON t.object_id = ic.object_id "
        "JOIN sys.schemas s ON s.schema_id = t.schema_id "
        "JOIN sys.columns c ON c.object_id = ic.object_id AND c.column_id = ic.column_id"
    )
    for schema, table, column, seed in cur.fetchall():
        full = f"[{schema}].[{table}]"
        cur.execute(f"SELECT MAX([{column}]) FROM {full}")
        max_id = cur.fetchone()[0]
        value = max_id if max_id is not None else seed - 1
        cur.execute(f"DBCC CHECKIDENT ('{schema}.{table}', RESEED, {value}) WITH NO_INFOMSGS")
    conn.commit()


def run_sql(sql, max_rows):
    conn = connect()
    cur = conn.cursor()
    parts = []
    messages = []
    try:
        for batch in GO_RE.split(sql):
            if not batch.strip():
                continue
            cur.execute(batch)
            while True:
                if cur.description:
                    cols = [d[0] for d in cur.description]
                    rows = cur.fetchall()
                    parts.append(render_table(cols, rows, max_rows))
                elif cur.rowcount and cur.rowcount > 0:
                    messages.append(cur.rowcount)
                if not cur.nextset():
                    break
    finally:
        conn.rollback()
        reseed(conn)
        conn.close()
    if not parts:
        total = sum(messages)
        return f'<p class="result-more">Запит виконано. Змінено рядків: {total}</p>'
    return "\n".join(parts)


def process(path):
    text = path.read_text(encoding="utf-8")
    errors = []

    def repl(m):
        sql = m.group("sql")
        opts = (m.group("opts") or "") + (m.group("opts2") or "")
        rows = 10
        rm = re.search(r"rows=(\d+)", opts)
        if rm:
            rows = int(rm.group(1))
        try:
            result = run_sql(sql, rows)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{path.name}: {e}\n---\n{sql}\n---")
            return m.group(0)
        opt_str = f" rows={rows}" if rm else ""
        return (
            m.group(1)
            + "\n"
            + f"<!-- run:start{opt_str} -->\n"
            + '<div class="result-label">Результат:</div>\n'
            + result
            + "\n<!-- run:end -->"
        )

    new = BLOCK_RE.sub(repl, text)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return errors


def check(path):
    text = path.read_text(encoding="utf-8")
    errors = []
    conn = connect(autocommit=True)
    cur = conn.cursor()
    for sql in SQL_BLOCK_RE.findall(text):
        for batch in GO_RE.split(sql):
            if not batch.strip():
                continue
            try:
                cur.execute("SET PARSEONLY ON")
                cur.execute(batch)
            except Exception as e:  # noqa: BLE001
                errors.append(f"{path.name}: {str(e)[:300]}\n---\n{batch.strip()[:400]}\n---")
            finally:
                try:
                    cur.execute("SET PARSEONLY OFF")
                except Exception:  # noqa: BLE001
                    conn.close()
                    conn = connect(autocommit=True)
                    cur = conn.cursor()
    conn.close()
    return errors


def main():
    mode_check = "--check" in sys.argv
    files = [Path(a) for a in sys.argv[1:] if not a.startswith("--")] or LESSONS
    all_errors = []
    for f in files:
        all_errors += check(f) if mode_check else process(f)
    for e in all_errors:
        print(e, file=sys.stderr)
    print(f"Файлів: {len(files)}, помилок: {len(all_errors)}")
    sys.exit(1 if all_errors else 0)


if __name__ == "__main__":
    main()
