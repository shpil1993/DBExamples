#!/usr/bin/env python3
"""Генерує довідники функцій (tutorial/*-functions.md).

Для кожної функції задано опис і вираз-приклад. Приклад виконується
на SQL Server, а отриманий результат записується в таблицю довідника.
Потрібні ті самі умови, що й для run_examples.py.
"""
import html
from pathlib import Path

from run_examples import connect, fmt

ROOT = Path(__file__).resolve().parent.parent

STRING = [
    ("ASCII", "Повертає ASCII-код першого символу рядка", "ASCII('A')"),
    ("CHAR", "Повертає символ за ASCII-кодом", "CHAR(65)"),
    ("CHARINDEX", "Повертає позицію підрядка в рядку (0, якщо не знайдено)", "CHARINDEX('t', 'Customer')"),
    ("CONCAT", "Об'єднує два або більше рядків (NULL замінюється на порожній рядок)", "CONCAT('SQL', ' ', 'Server')"),
    ("CONCAT_WS", "Об'єднує рядки через роздільник", "CONCAT_WS('-', '2024', '07', '08')"),
    ("DATALENGTH", "Повертає кількість байтів, які займає вираз", "DATALENGTH(N'Київ')"),
    ("DIFFERENCE", "Порівнює два значення SOUNDEX і повертає число від 0 до 4", "DIFFERENCE('Juice', 'Jucy')"),
    ("FORMAT", "Форматує значення за шаблоном і культурою", "FORMAT(1234567.891, 'N2', 'uk-UA')"),
    ("LEFT", "Повертає задану кількість символів з початку рядка", "LEFT('SQL Server', 3)"),
    ("LEN", "Повертає довжину рядка (без кінцевих пробілів)", "LEN('SQL Server  ')"),
    ("LOWER", "Перетворює рядок на нижній регістр", "LOWER('SQL Server')"),
    ("LTRIM", "Видаляє пробіли на початку рядка", "LTRIM('   SQL')"),
    ("NCHAR", "Повертає символ Unicode за кодом", "NCHAR(1028)"),
    ("PATINDEX", "Повертає позицію першого входження шаблону", "PATINDEX('%[0-9]%', 'abc123')"),
    ("QUOTENAME", "Бере рядок у роздільники, роблячи його коректним ідентифікатором", "QUOTENAME('my table')"),
    ("REPLACE", "Замінює всі входження підрядка іншим рядком", "REPLACE('SQL Tutorial', 'Tutorial', 'Server')"),
    ("REPLICATE", "Повторює рядок задану кількість разів", "REPLICATE('ab', 3)"),
    ("REVERSE", "Перевертає рядок", "REVERSE('SQL')"),
    ("RIGHT", "Повертає задану кількість символів з кінця рядка", "RIGHT('SQL Server', 6)"),
    ("RTRIM", "Видаляє пробіли в кінці рядка", "RTRIM('SQL   ') + '|'"),
    ("SOUNDEX", "Повертає чотирисимвольний фонетичний код рядка", "SOUNDEX('Juice')"),
    ("SPACE", "Повертає рядок із заданої кількості пробілів", "'[' + SPACE(3) + ']'"),
    ("STR", "Перетворює число на рядок", "STR(185.476, 6, 2)"),
    ("STRING_AGG", "Об'єднує значення рядків групи через роздільник (2017+)", "(SELECT STRING_AGG(ShipperName, ', ') FROM Shippers)"),
    ("STRING_SPLIT", "Таблична функція: розбиває рядок на рядки за роздільником (2016+)", "(SELECT COUNT(*) FROM STRING_SPLIT('a,b,c', ','))"),
    ("STUFF", "Видаляє частину рядка і вставляє на її місце інший рядок", "STUFF('SQL Tutorial', 1, 3, 'T-SQL')"),
    ("SUBSTRING", "Повертає частину рядка", "SUBSTRING('SQL Server', 5, 6)"),
    ("TRANSLATE", "Посимвольно замінює символи (2017+)", "TRANSLATE('2*[3+4]', '[]', '()')"),
    ("TRIM", "Видаляє пробіли (або задані символи) з обох кінців рядка (2017+)", "'|' + TRIM('   SQL   ') + '|'"),
    ("UNICODE", "Повертає код Unicode першого символу", "UNICODE(N'Ї')"),
    ("UPPER", "Перетворює рядок на верхній регістр", "UPPER('SQL Server')"),
]

NUMERIC = [
    ("ABS", "Повертає абсолютне значення числа", "ABS(-243.5)"),
    ("ACOS", "Повертає арккосинус числа", "ACOS(0.25)"),
    ("ASIN", "Повертає арксинус числа", "ASIN(0.25)"),
    ("ATAN", "Повертає арктангенс числа", "ATAN(2.5)"),
    ("ATN2", "Повертає арктангенс двох чисел", "ATN2(0.50, 1)"),
    ("AVG", "Агрегатна: середнє значення виразу", "(SELECT AVG(Price) FROM Products)"),
    ("CEILING", "Найменше ціле, яке більше або дорівнює числу", "CEILING(25.75)"),
    ("COUNT", "Агрегатна: кількість рядків", "(SELECT COUNT(*) FROM Products)"),
    ("COS", "Повертає косинус числа", "COS(2)"),
    ("COT", "Повертає котангенс числа", "COT(6)"),
    ("DEGREES", "Перетворює радіани на градуси", "DEGREES(PI())"),
    ("EXP", "Повертає e в заданому степені", "EXP(1)"),
    ("FLOOR", "Найбільше ціле, яке менше або дорівнює числу", "FLOOR(25.75)"),
    ("LOG", "Натуральний логарифм (або логарифм за заданою основою)", "LOG(8, 2)"),
    ("LOG10", "Десятковий логарифм", "LOG10(1000)"),
    ("MAX", "Агрегатна: найбільше значення", "(SELECT MAX(Price) FROM Products)"),
    ("MIN", "Агрегатна: найменше значення", "(SELECT MIN(Price) FROM Products)"),
    ("PI", "Повертає число π", "PI()"),
    ("POWER", "Підносить число до степеня", "POWER(4, 2)"),
    ("RADIANS", "Перетворює градуси на радіани", "RADIANS(180.0)"),
    ("RAND", "Повертає випадкове число від 0 до 1 (з seed — передбачуване)", "RAND(5)"),
    ("ROUND", "Округлює число до заданої кількості знаків", "ROUND(235.415, 2)"),
    ("SIGN", "Повертає знак числа: -1, 0 або 1", "SIGN(-255.5)"),
    ("SIN", "Повертає синус числа", "SIN(2)"),
    ("SQRT", "Повертає квадратний корінь", "SQRT(64)"),
    ("SQUARE", "Повертає квадрат числа", "SQUARE(64)"),
    ("SUM", "Агрегатна: сума значень", "(SELECT SUM(Quantity) FROM OrderDetails)"),
    ("TAN", "Повертає тангенс числа", "TAN(1.75)"),
]

DATE = [
    ("CURRENT_TIMESTAMP", "Поточна дата й час (стандарт SQL, аналог GETDATE)", None),
    ("DATEADD", "Додає інтервал до дати", "DATEADD(MONTH, 2, '2024-07-08')"),
    ("DATEDIFF", "Повертає різницю між двома датами у вказаних одиницях", "DATEDIFF(DAY, '2024-07-08', '2024-12-31')"),
    ("DATEDIFF_BIG", "Як DATEDIFF, але повертає BIGINT", "DATEDIFF_BIG(SECOND, '2000-01-01', '2024-01-01')"),
    ("DATEFROMPARTS", "Створює дату з року, місяця й дня", "DATEFROMPARTS(2024, 8, 24)"),
    ("DATENAME", "Повертає назву частини дати як рядок", "DATENAME(MONTH, '2024-07-08')"),
    ("DATEPART", "Повертає частину дати як ціле число", "DATEPART(QUARTER, '2024-07-08')"),
    ("DATETRUNC", "Обрізає дату до вказаної частини (2022+)", "DATETRUNC(MONTH, CAST('2024-07-08' AS DATE))"),
    ("DATETIMEFROMPARTS", "Створює DATETIME з частин", "DATETIMEFROMPARTS(2024, 7, 8, 14, 30, 0, 0)"),
    ("DAY", "Повертає день місяця", "DAY('2024-07-08')"),
    ("EOMONTH", "Повертає останній день місяця", "EOMONTH('2024-02-10')"),
    ("GETDATE", "Поточна дата й час сервера (DATETIME)", None),
    ("GETUTCDATE", "Поточна дата й час UTC (DATETIME)", None),
    ("ISDATE", "Перевіряє, чи є рядок коректною датою (1 або 0)", "ISDATE('2024-02-30')"),
    ("MONTH", "Повертає місяць", "MONTH('2024-07-08')"),
    ("SYSDATETIME", "Поточна дата й час з високою точністю (DATETIME2)", None),
    ("SYSDATETIMEOFFSET", "Поточна дата й час з часовим поясом", None),
    ("SYSUTCDATETIME", "Поточна дата й час UTC (DATETIME2)", None),
    ("SWITCHOFFSET", "Змінює часовий пояс значення DATETIMEOFFSET", "SWITCHOFFSET(CAST('2024-07-08 12:00 +00:00' AS DATETIMEOFFSET), '+03:00')"),
    ("TODATETIMEOFFSET", "Додає часовий пояс до DATETIME2", "TODATETIMEOFFSET(CAST('2024-07-08 12:00' AS DATETIME2(0)), '+02:00')"),
    ("YEAR", "Повертає рік", "YEAR('2024-07-08')"),
]

ADVANCED = [
    ("CAST", "Перетворює значення в інший тип даних", "CAST('25.65' AS DECIMAL(5,1))"),
    ("COALESCE", "Повертає перше значення зі списку, що не є NULL", "COALESCE(NULL, NULL, 'SQL', 'Server')"),
    ("CONVERT", "Перетворює значення в інший тип (зі стилем форматування)", "CONVERT(VARCHAR(10), CAST('2024-07-08' AS DATE), 104)"),
    ("CURRENT_USER", "Ім'я поточного користувача бази даних", "CURRENT_USER"),
    ("DB_NAME", "Ім'я поточної (або заданої) бази даних", "DB_NAME()"),
    ("CHOOSE", "Повертає елемент списку за індексом", "CHOOSE(2, 'red', 'green', 'blue')"),
    ("GREATEST", "Найбільше значення зі списку (2022+)", "GREATEST(5, 12, 3)"),
    ("IIF", "Повертає одне з двох значень залежно від умови", "IIF(500 < 1000, 'YES', 'NO')"),
    ("ISNULL", "Повертає заміну, якщо вираз дорівнює NULL", "ISNULL(NULL, 'SQL Server')"),
    ("ISNUMERIC", "Перевіряє, чи є вираз числом (1 або 0)", "ISNUMERIC('4567')"),
    ("LEAST", "Найменше значення зі списку (2022+)", "LEAST(5, 12, 3)"),
    ("NEWID", "Генерує новий унікальний ідентифікатор (GUID)", None),
    ("NULLIF", "Повертає NULL, якщо два вирази рівні", "NULLIF(25, 25)"),
    ("OBJECT_ID", "Ідентифікатор об'єкта бази даних за іменем", "CASE WHEN OBJECT_ID('dbo.Customers') IS NOT NULL THEN 'exists' END"),
    ("SESSION_USER", "Ім'я користувача в поточному сеансі", "SESSION_USER"),
    ("SESSIONPROPERTY", "Значення параметра сеансу", "SESSIONPROPERTY('ANSI_NULLS')"),
    ("SYSTEM_USER", "Ім'я логіна", "SYSTEM_USER"),
    ("TRY_CAST", "Як CAST, але повертає NULL замість помилки", "TRY_CAST('abc' AS INT)"),
    ("TRY_CONVERT", "Як CONVERT, але повертає NULL замість помилки", "TRY_CONVERT(DATE, '2024-13-45')"),
    ("TRY_PARSE", "Перетворює рядок з урахуванням культури, NULL при помилці", "TRY_PARSE('08.07.2024' AS DATE USING 'uk-UA')"),
    ("USER_NAME", "Ім'я користувача бази даних за ідентифікатором", "USER_NAME()"),
    ("@@ROWCOUNT", "Кількість рядків, оброблених останньою інструкцією", None),
    ("@@VERSION", "Версія SQL Server", None),
    ("JSON_VALUE", "Витягує скалярне значення з JSON", "JSON_VALUE('{\"city\":\"Kyiv\"}', '$.city')"),
    ("ISJSON", "Перевіряє, чи є рядок коректним JSON", "ISJSON('{\"a\":1}')"),
]

PAGES = {
    "string-functions.md": (
        "Рядкові функції",
        "Рядкові функції SQL Server",
        "Функції для роботи з текстом: пошук, заміна, вирізання частин рядка, зміна регістру тощо.",
        STRING,
    ),
    "numeric-functions.md": (
        "Числові функції",
        "Числові та математичні функції SQL Server",
        "Математичні функції та агрегатні функції для чисел.",
        NUMERIC,
    ),
    "date-functions.md": (
        "Функції дати й часу",
        "Функції дати й часу SQL Server",
        "Функції для отримання поточної дати, виділення частин дати, арифметики дат і форматування. "
        "Детальніше про роботу з датами — в уроці [Робота з датами](dates.html).",
        DATE,
    ),
    "advanced-functions.md": (
        "Інші функції",
        "Функції перетворення та системні функції",
        "Функції перетворення типів, роботи з NULL, умовні та системні функції.",
        ADVANCED,
    ),
}

DATE_PARTS = """
## Частини дати (datepart)

Функції `DATEADD`, `DATEDIFF`, `DATENAME`, `DATEPART` і `DATETRUNC` приймають такі назви частин дати:

| Частина | Скорочення |
|---|---|
| `YEAR` | `yy`, `yyyy` |
| `QUARTER` | `qq`, `q` |
| `MONTH` | `mm`, `m` |
| `DAYOFYEAR` | `dy`, `y` |
| `DAY` | `dd`, `d` |
| `WEEK` | `wk`, `ww` |
| `WEEKDAY` | `dw` |
| `HOUR` | `hh` |
| `MINUTE` | `mi`, `n` |
| `SECOND` | `ss`, `s` |
| `MILLISECOND` | `ms` |
| `MICROSECOND` | `mcs` |
| `NANOSECOND` | `ns` |

## Стилі CONVERT для дат

| Стиль | Формат | Приклад |
|---|---|---|
| 23 | `yyyy-mm-dd` | `CONVERT(VARCHAR, @d, 23)` → 2024-07-08 |
| 104 | `dd.mm.yyyy` | `CONVERT(VARCHAR, @d, 104)` → 08.07.2024 |
| 103 | `dd/mm/yyyy` | `CONVERT(VARCHAR, @d, 103)` → 08/07/2024 |
| 101 | `mm/dd/yyyy` | `CONVERT(VARCHAR, @d, 101)` → 07/08/2024 |
| 112 | `yyyymmdd` | `CONVERT(VARCHAR, @d, 112)` → 20240708 |
| 120 | `yyyy-mm-dd hh:mi:ss` | `CONVERT(VARCHAR, @dt, 120)` → 2024-07-08 14:30:00 |
"""


def evaluate(cur, expr):
    cur.execute(f"SELECT {expr}")
    return cur.fetchone()[0]


def build():
    conn = connect(autocommit=True)
    cur = conn.cursor()
    for filename, (title, h1, intro, items) in PAGES.items():
        lines = [
            "---",
            f"title: "{title}"",
            f"h1: "{h1}"",
            "---",
            "",
            intro,
            "",
            "Колонка «Результат» отримана виконанням прикладу на SQL Server 2022 з демо-базою DemoShop.",
            "",
            '<div class="table-scroll"><table>',
            "<tr><th>Функція</th><th>Опис</th><th>Приклад</th><th>Результат</th></tr>",
        ]
        for name, desc, expr in items:
            if expr is None:
                call = name if name.startswith("@@") or name == "CURRENT_TIMESTAMP" else name + "()"
                example = f"<code>SELECT {call};</code>"
                result = '<span class="null">залежить від сервера</span>'
            else:
                example = f"<code>SELECT {html.escape(expr, quote=False)};</code>"
                result = fmt(evaluate(cur, expr))
            lines.append(
                f"<tr><td><strong>{name}</strong></td><td>{html.escape(desc, quote=False)}</td>"
                f"<td>{example}</td><td>{result}</td></tr>"
            )
        lines.append("</table></div>")
        if filename == "date-functions.md":
            lines.append(DATE_PARTS)
        (ROOT / "tutorial" / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{filename}: {len(items)} функцій")
    conn.close()


if __name__ == "__main__":
    build()
