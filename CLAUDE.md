# CLAUDE.md

Контекст для роботи з цим репозиторієм.

## Що це

Навчальний курс **Microsoft SQL Server / T-SQL українською мовою**, побудований за структурою підручника MySQL на W3Schools, **без вправ і тестів**. Це статичний сайт на Jekyll, який публікується на GitHub Pages: https://shpil1993.github.io/DBExamples/

* Усі тексти сайту — українською. Терміни SQL і код залишаються англійською.
* Приклади працюють з навчальною базою **DemoShop** (спрощена Northwind): `assets/sql/demo-db.sql`.
* Результати під прикладами — **реальні**: їх отримано виконанням запитів на SQL Server 2022, а не написано вручну.

## Структура

| Шлях | Призначення |
|---|---|
| `_data/nav.yml` | Меню і **порядок уроків**: кнопки «Попередній / Наступний» обчислюються з цього списку |
| `_layouts/default.html` | Єдиний шаблон: верхня панель, бокове меню з пошуком, пейджер |
| `assets/css/style.css` | Стилі; кольори задано змінними в `:root`, темна тема — `prefers-color-scheme` і `[data-theme="dark"]` |
| `assets/js/main.js` | Перемикач теми, мобільне меню, пошук у меню, кнопка «Копіювати» |
| `assets/sql/demo-db.sql` | Скрипт демо-бази (видаляє і створює `DemoShop` заново) |
| `index.md` | Головна сторінка зі змістом курсу |
| `tutorial/*.md` | Уроки (72 сторінки) |
| `tutorial/{string,numeric,date,advanced}-functions.md` | **Згенеровані** файли — не редагувати вручну, див. `tools/build_functions.py` |
| `tools/run_examples.py` | Виконує приклади й вставляє результати в уроки |
| `tools/build_functions.py` | Генерує довідники функцій |
| `.github/workflows/pages.yml` | Збирання і публікація на GitHub Pages при push у `main` |

## Формат уроку

```markdown
---
title: "Коротка назва для меню і <title>"
h1: "Заголовок сторінки (необов'язково, інакше береться title)"
---

Вступний абзац.

## Синтаксис

```sql
SELECT column1 FROM table_name;
```

<div class="example" markdown="1">

Пояснення прикладу:

```sql
SELECT CustomerName FROM Customers WHERE Country = N'Germany';
```
<!-- run -->

</div>
```

Правила:

* Значення `title` і `h1` у front matter **завжди беріть у лапки**: двокрапка без лапок ламає YAML.
* Блоки: `<div class="example" markdown="1">`, `<div class="note" markdown="1">`, `<div class="warn" markdown="1">`. Атрибут `markdown="1"` обов'язковий, інакше Markdown усередині не обробляється.
* Рядкові літерали в прикладах пишуться з префіксом `N` (`N'Kyiv'`), дати — у форматі `'YYYY-MM-DD'`.
* Блоки синтаксису (`column_name`, `table_name`, `...`) пишуться без маркера `<!-- run -->`.
* Посилання між уроками відносні: `[JOIN](joins.html)`.
* Новий урок: створіть `tutorial/<name>.md` **і** додайте його в `_data/nav.yml` у потрібне місце.
* Якщо урок порівнює SQL Server з MySQL, відмінності показуються в окремій примітці (`note`).

## Виконання прикладів (`<!-- run -->`)

Маркер `<!-- run -->` (або `<!-- run rows=20 -->`) одразу після блоку ```` ```sql ```` означає: виконати запит і вставити результат. Скрипт замінює маркер на блок `<!-- run:start --> … <!-- run:end -->`; повторний запуск оновлює цей блок.

* Кожен приклад виконується в транзакції з **відкатом**, тому база не змінюється. Після кожного прикладу лічильники `IDENTITY` повертаються до початкових значень.
* Між DDL та інструкціями, що використовують його результат (новий стовпець, `CREATE VIEW/PROCEDURE/FUNCTION/TRIGGER`), потрібен рядок `GO`. Скрипт розбиває текст на пакети за `GO`.
* Приклади, які самі виконують `ROLLBACK` або `COMMIT` (наприклад, `TRY...CATCH` з транзакцією), конфліктують з транзакцією-обгорткою. Для них маркер не ставиться: такий приклад виконується окремо (наприклад, у `tempdb`), а результат вставляється вручну (див. `tutorial/transactions.md`).
* Після зміни прикладу перевіряйте, що текст уроку відповідає результату: наприклад, порожній результат там, де текст обіцяє рядки.

### Локальний SQL Server

```bash
dockerd > /tmp/dockerd.log 2>&1 &          # якщо демон Docker не запущено
docker run -d --name mssql -e ACCEPT_EULA=Y -e 'MSSQL_SA_PASSWORD=Str0ng!Passw0rd' \
  -p 1433:1433 mcr.microsoft.com/mssql/server:2022-latest
docker cp assets/sql/demo-db.sql mssql:/tmp/demo.sql
docker exec mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P 'Str0ng!Passw0rd' -C -b -i /tmp/demo.sql
pip install pymssql
```

Скрипти читають змінні `MSSQL_HOST`, `MSSQL_USER`, `MSSQL_PASSWORD` (за замовчуванням `localhost`, `sa`, `Str0ng!Passw0rd`).

```bash
python3 tools/run_examples.py                      # усі уроки
python3 tools/run_examples.py tutorial/joins.md    # окремі файли
python3 tools/run_examples.py --check              # SET PARSEONLY для блоків без маркера
python3 tools/build_functions.py                   # перегенерувати довідники функцій
```

`--check` очікувано повідомляє про помилки в шаблонах синтаксису (`column_name`, `...`, `condition`) і в навмисних прикладах помилок. Звертайте увагу лише на справжній код.

Довідники функцій змінюються в списках `STRING`, `NUMERIC`, `DATE`, `ADVANCED` у `tools/build_functions.py` (назва, опис, вираз-приклад; `None` — якщо результат залежить від сервера). Після змін запустіть генератор.

## Збирання сайту

GitHub Pages використовує gem `github-pages` (**Jekyll 3.10**, kramdown GFM, Rouge). Локально перевіряйте саме ним:

```bash
bundle config set --local path vendor/bundle
bundle install
LANG=C.UTF-8 bundle exec jekyll build      # або: bundle exec jekyll serve
# http://localhost:4000/DBExamples/
```

* `baseurl: /DBExamples`. У шаблонах посилання будуються через `| relative_url`.
* `vendor`, `tools`, `Gemfile*`, `README.md`, `CLAUDE.md` виключено зі збирання в `_config.yml`. Без виключення `vendor` збирання падає на SCSS теми.
* Після збирання варто перевірити, що в `_site` немає битих внутрішніх посилань, і переглянути сторінки на ширині телефону (Playwright і Chromium встановлено, `NODE_PATH=/opt/node22/lib/node_modules`).

## Публікація

* Push у `main` запускає `.github/workflows/pages.yml`, який збирає й публікує сайт.
* У налаштуваннях репозиторію має бути **Settings → Pages → Source: GitHub Actions**.
* Робоча гілка для змін — `claude/trusting-sagan-fgq8j6`; `main` оновлюється лише з дозволу власника репозиторію.
