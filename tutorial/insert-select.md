---
title: INSERT INTO SELECT
h1: Інструкція INSERT INTO SELECT
---

Інструкція `INSERT INTO SELECT` копіює дані з однієї таблиці та вставляє їх в **іншу, вже існуючу** таблицю.

* Типи даних у джерелі та цільовій таблиці мають бути сумісними.
* Наявні записи в цільовій таблиці не змінюються.

## Синтаксис

Скопіювати всі стовпці:

```sql
INSERT INTO table2
SELECT * FROM table1
WHERE condition;
```

Скопіювати лише деякі стовпці:

```sql
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
```

## Приклади

<div class="example" markdown="1">

Додати всіх постачальників як клієнтів (стовпці, яких немає в `Suppliers`, отримають `NULL`):

```sql
INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 6</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Додати як клієнтів лише постачальників з Японії:

```sql
INSERT INTO Customers (CustomerName, ContactName, City, Country)
SELECT SupplierName, ContactName, City, Country
FROM Suppliers
WHERE Country = N'Japan';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 1</p>
<!-- run:end -->

</div>

## SELECT INTO чи INSERT INTO SELECT?

| | `SELECT INTO` | `INSERT INTO SELECT` |
|---|---|---|
| Цільова таблиця | **Створюється** автоматично | Повинна **вже існувати** |
| Можна вибрати типи й обмеження стовпців | Ні | Так (задаються в `CREATE TABLE`) |
| Типове використання | Швидка копія, тимчасові таблиці | Перенесення даних у готову структуру |

## INSERT ... EXEC

У T-SQL у таблицю можна вставити також результат виконання збереженої процедури:

```sql
INSERT INTO table_name (column1, column2)
EXEC procedure_name;
```
