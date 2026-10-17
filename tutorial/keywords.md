---
title: "Ключові слова"
h1: "Ключові слова T-SQL"
---

Перелік основних ключових слів T-SQL, що розглядаються в курсі, з посиланнями на уроки.

| Ключове слово | Опис |
|---|---|
| [`ADD`](alter-table.html) | Додає стовпець або обмеження до існуючої таблиці |
| [`ADD CONSTRAINT`](constraints.html) | Додає обмеження до існуючої таблиці |
| [`ALL`](any-all.html) | TRUE, якщо умова виконується для всіх значень підзапиту |
| [`ALTER COLUMN`](alter-table.html) | Змінює тип даних стовпця |
| [`ALTER TABLE`](alter-table.html) | Додає, видаляє або змінює стовпці та обмеження таблиці |
| [`ALTER VIEW`](views.html) | Змінює представлення |
| [`AND`](and-or-not.html) | Повертає рядки, для яких обидві умови істинні |
| [`ANY`](any-all.html) | TRUE, якщо умова виконується хоча б для одного значення підзапиту |
| [`AS`](aliases.html) | Задає псевдонім стовпця або таблиці |
| [`ASC`](order-by.html) | Сортування за зростанням |
| [`BACKUP DATABASE`](backup-db.html) | Створює резервну копію бази даних |
| [`BEGIN TRANSACTION`](transactions.html) | Починає транзакцію |
| [`BEGIN...END`](control-flow.html) | Об'єднує інструкції в блок |
| [`BETWEEN`](between.html) | Вибирає значення в заданому діапазоні |
| [`CASE`](case.html) | Повертає різні значення залежно від умов |
| [`CHECK`](check.html) | Обмеження, що перевіряє умову для значень |
| [`COLUMN`](alter-table.html) | Використовується в `DROP COLUMN`, `ALTER COLUMN` |
| [`COMMIT`](transactions.html) | Підтверджує транзакцію |
| [`CONSTRAINT`](constraints.html) | Задає ім'я обмеження |
| [`CREATE DATABASE`](create-db.html) | Створює базу даних |
| [`CREATE FUNCTION`](user-functions.html) | Створює функцію користувача |
| [`CREATE INDEX`](create-index.html) | Створює індекс (дозволяє повторювані значення) |
| [`CREATE OR ALTER`](views.html) | Створює об'єкт або змінює наявний |
| [`CREATE PROCEDURE`](stored-procedures.html) | Створює збережену процедуру |
| [`CREATE TABLE`](create-table.html) | Створює таблицю |
| [`CREATE TRIGGER`](triggers.html) | Створює тригер |
| [`CREATE UNIQUE INDEX`](create-index.html) | Створює унікальний індекс |
| [`CREATE VIEW`](views.html) | Створює представлення |
| [`CROSS APPLY`](cross-join.html) | Виконує табличний вираз для кожного рядка лівої таблиці |
| [`CROSS JOIN`](cross-join.html) | Повертає всі комбінації рядків двох таблиць |
| [`DECLARE`](variables.html) | Оголошує змінну |
| [`DEFAULT`](default.html) | Задає значення за замовчуванням |
| [`DELETE`](delete.html) | Видаляє рядки з таблиці |
| [`DESC`](order-by.html) | Сортування за спаданням |
| [`DISTINCT`](distinct.html) | Вибирає лише унікальні значення |
| [`DROP COLUMN`](alter-table.html) | Видаляє стовпець |
| [`DROP CONSTRAINT`](constraints.html) | Видаляє обмеження |
| [`DROP DATABASE`](drop-db.html) | Видаляє базу даних |
| [`DROP INDEX`](create-index.html) | Видаляє індекс |
| [`DROP TABLE`](drop-table.html) | Видаляє таблицю |
| [`DROP VIEW`](views.html) | Видаляє представлення |
| [`EXCEPT`](union.html) | Рядки першого запиту, яких немає в другому |
| [`EXEC`](stored-procedures.html) | Виконує збережену процедуру |
| [`EXISTS`](exists.html) | Перевіряє наявність рядків у підзапиті |
| [`FOREIGN KEY`](foreign-key.html) | Обмеження зовнішнього ключа |
| [`FROM`](select.html) | Вказує таблицю, з якої вибираються дані |
| [`FULL OUTER JOIN`](full-join.html) | Повертає всі рядки обох таблиць |
| [`GO`](variables.html) | Роздільник пакетів (команда клієнта) |
| [`GROUP BY`](group-by.html) | Групує результат для агрегатних функцій |
| [`HAVING`](having.html) | Фільтрує групи (замість `WHERE` для агрегатів) |
| [`IDENTITY`](identity.html) | Автоматично генерує числа для стовпця |
| [`IF...ELSE`](control-flow.html) | Умовне виконання |
| [`IN`](in.html) | Перевіряє, чи входить значення до списку |
| [`INNER JOIN`](inner-join.html) | Повертає рядки, що мають збіг в обох таблицях |
| [`INSERT INTO`](insert.html) | Додає нові рядки в таблицю |
| [`INSERT INTO SELECT`](insert-select.html) | Копіює дані з однієї таблиці в іншу |
| [`INTERSECT`](union.html) | Рядки, що є в обох запитах |
| [`IS NULL`](null-values.html) | Перевіряє значення на `NULL` |
| [`IS NOT NULL`](null-values.html) | Перевіряє, що значення не `NULL` |
| [`JOIN`](joins.html) | З'єднує таблиці |
| [`LEFT JOIN`](left-join.html) | Усі рядки лівої таблиці та збіги з правої |
| [`LIKE`](like.html) | Пошук за шаблоном |
| [`NOT`](and-or-not.html) | Заперечення умови |
| [`NOT NULL`](not-null.html) | Забороняє значення `NULL` у стовпці |
| [`OFFSET ... FETCH`](top.html) | Пропускає та повертає задану кількість рядків |
| [`OR`](and-or-not.html) | Повертає рядки, для яких хоча б одна умова істинна |
| [`ORDER BY`](order-by.html) | Сортує результат |
| [`OUTPUT`](insert.html) | Повертає змінені рядки з `INSERT`, `UPDATE`, `DELETE` |
| [`OVER`](cte-window.html) | Задає вікно для віконних функцій |
| [`PRIMARY KEY`](primary-key.html) | Первинний ключ таблиці |
| [`PRINT`](variables.html) | Виводить повідомлення |
| [`RESTORE DATABASE`](backup-db.html) | Відновлює базу з резервної копії |
| [`RIGHT JOIN`](right-join.html) | Усі рядки правої таблиці та збіги з лівої |
| [`ROLLBACK`](transactions.html) | Відкочує транзакцію |
| [`SELECT`](select.html) | Вибирає дані з бази даних |
| [`SELECT DISTINCT`](distinct.html) | Вибирає лише унікальні значення |
| [`SELECT INTO`](select-into.html) | Створює нову таблицю з результату запиту |
| [`SET`](update.html) | Задає значення в `UPDATE` або змінній |
| [`THROW`](try-catch.html) | Генерує помилку |
| [`TOP`](top.html) | Обмежує кількість рядків результату |
| [`TRUNCATE TABLE`](delete.html) | Видаляє всі рядки таблиці |
| [`TRY...CATCH`](try-catch.html) | Обробка помилок |
| [`UNION`](union.html) | Об'єднує результати запитів (без дублікатів) |
| [`UNION ALL`](union.html) | Об'єднує результати запитів (з дублікатами) |
| [`UNIQUE`](unique.html) | Обмеження унікальності значень |
| [`UPDATE`](update.html) | Змінює рядки таблиці |
| [`USE`](create-db.html) | Перемикає поточну базу даних |
| [`VALUES`](insert.html) | Задає значення для `INSERT` |
| [`VIEW`](views.html) | Представлення (віртуальна таблиця) |
| [`WHERE`](where.html) | Фільтрує рядки |
| [`WHILE`](control-flow.html) | Цикл |
| [`WITH`](cte-window.html) | Оголошує загальний табличний вираз (CTE) |
