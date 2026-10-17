---
title: "INSERT INTO"
h1: "Інструкція INSERT INTO"
---

Інструкція `INSERT INTO` додає нові записи до таблиці.

## Синтаксис

Записати `INSERT INTO` можна двома способами.

**1. Із зазначенням стовпців і значень:**

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

**2. Без переліку стовпців** — тоді значення треба вказати для **всіх** стовпців у тому порядку, у якому вони йдуть у таблиці (крім стовпців `IDENTITY`):

```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

<div class="note" markdown="1">
Завжди краще явно перелічувати стовпці: такий код зрозуміліший і не зламається, якщо структура таблиці зміниться.
</div>

## Приклад

<div class="example" markdown="1">

Додати нового клієнта:

```sql
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (N'Cardinal', N'Tom B. Erichsen', N'Skagen 21', N'Stavanger', N'4006', N'Norway');
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 1</p>
<!-- run:end -->

</div>

Стовпець `CustomerID` — автоінкрементний (`IDENTITY`), тому його значення генерується автоматично і вказувати його не потрібно.

## Додавання значень лише в деякі стовпці

Можна вказати лише частину стовпців. Решта отримає значення за замовчуванням (`DEFAULT`) або `NULL`:

<div class="example" markdown="1">

```sql
INSERT INTO Customers (CustomerName, City, Country)
VALUES (N'Kharkiv Foods', N'Kharkiv', N'Ukraine');

SELECT CustomerID, CustomerName, ContactName, City, Country
FROM Customers
WHERE CustomerName = N'Kharkiv Foods';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>ContactName</th><th>City</th><th>Country</th></tr>
<tr><td>14</td><td>Kharkiv Foods</td><td><span class="null">NULL</span></td><td>Kharkiv</td><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Додавання кількох рядків

Одна інструкція `INSERT` може додати кілька рядків (до 1000) — перелічіть набори значень через кому:

<div class="example" markdown="1">

```sql
INSERT INTO Shippers (ShipperName, Phone)
VALUES
    (N'Nova Poshta', N'+380 800 500 609'),
    (N'Ukrposhta',   N'+380 800 300 545'),
    (N'Meest',       N'+380 800 504 400');
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 3</p>
<!-- run:end -->

</div>

## Отримання згенерованого ідентифікатора

Щоб дізнатися значення `IDENTITY` щойно доданого рядка, використовуйте функцію `SCOPE_IDENTITY()` або конструкцію `OUTPUT`:

<div class="example" markdown="1">

```sql
INSERT INTO Categories (CategoryName, Description)
OUTPUT inserted.CategoryID, inserted.CategoryName
VALUES (N'Snacks', N'Chips, nuts and crackers');
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CategoryID</th><th>CategoryName</th></tr>
<tr><td>9</td><td>Snacks</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

```sql
INSERT INTO Categories (CategoryName) VALUES (N'Frozen');
SELECT SCOPE_IDENTITY() AS NewCategoryID;
```

<div class="note" markdown="1">
Приклади на цьому сайті, які змінюють дані, виконувалися в транзакції з відкатом, тому демо-база не змінилася. У вашій копії бази дані після виконання прикладу дійсно зміняться. Повернути початковий стан можна, повторно запустивши [скрипт демо-бази](demo-db.html).
</div>
