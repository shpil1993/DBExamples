# Підручник SQL Server

Безкоштовний курс з Microsoft SQL Server і T-SQL українською мовою, побудований за структурою підручника MySQL на W3Schools (без вправ і тестів).

Сайт: https://shpil1993.github.io/DBExamples/

## Зміст

* **Підручник SQL Server** — вступ, RDBMS, встановлення, демо-база даних.
* **SQL у SQL Server** — SELECT, WHERE, ORDER BY, INSERT, UPDATE, DELETE, TOP/OFFSET FETCH, агрегатні функції, LIKE, IN, BETWEEN, усі види JOIN, UNION, GROUP BY, HAVING, EXISTS, ANY/ALL, CASE, функції для NULL тощо.
* **База даних SQL Server** — CREATE/DROP/BACKUP DATABASE, CREATE/ALTER/DROP TABLE, обмеження, індекси, IDENTITY, дати, представлення, SQL-ін'єкції.
* **Програмування на T-SQL** — змінні, IF/WHILE, збережені процедури, функції, тригери, транзакції, TRY...CATCH, CTE та віконні функції.
* **Довідники** — типи даних, рядкові, числові, дата/час та інші функції, ключові слова.

Усі приклади працюють з демо-базою [`assets/sql/demo-db.sql`](assets/sql/demo-db.sql).

## Структура репозиторію

| Шлях | Призначення |
|---|---|
| `_config.yml` | Налаштування Jekyll |
| `_data/nav.yml` | Меню та порядок уроків |
| `_layouts/default.html` | Шаблон сторінки |
| `assets/` | Стилі, скрипти, SQL-скрипт демо-бази |
| `tutorial/*.md` | Уроки |
| `tools/run_examples.py` | Виконує приклади на SQL Server і вставляє результати в уроки |
| `tools/build_functions.py` | Генерує довідники функцій з реальними результатами |

## Публікація на GitHub Pages

Сайт збирається Jekyll і публікується workflow `.github/workflows/pages.yml` при кожному push у гілку `main`.

Одноразове налаштування: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

## Локальний перегляд

```bash
bundle install
bundle exec jekyll serve
# http://localhost:4000/DBExamples/
```

## Оновлення результатів прикладів

Блок ` ```sql ` з маркером `<!-- run -->` після нього виконується на базі DemoShop у транзакції з відкатом, а результат вставляється в урок.

```bash
docker run -d --name mssql -e ACCEPT_EULA=Y -e 'MSSQL_SA_PASSWORD=Str0ng!Passw0rd' \
  -p 1433:1433 mcr.microsoft.com/mssql/server:2022-latest
sqlcmd -S localhost,1433 -U sa -P 'Str0ng!Passw0rd' -C -i assets/sql/demo-db.sql
pip install pymssql

python3 tools/run_examples.py            # оновити результати в усіх уроках
python3 tools/run_examples.py --check    # перевірити синтаксис решти блоків
python3 tools/build_functions.py         # перегенерувати довідники функцій
```
