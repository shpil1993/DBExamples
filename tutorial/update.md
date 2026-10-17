---
title: "UPDATE"
h1: "Інструкція UPDATE"
---

Інструкція `UPDATE` змінює наявні записи в таблиці.

## Синтаксис

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

<div class="warn" markdown="1">
**Будьте уважні при оновленні записів!** Умова `WHERE` визначає, які рядки будуть змінені. Якщо пропустити `WHERE`, будуть оновлені **всі** рядки таблиці!
</div>

## Приклад

<div class="example" markdown="1">

Змінити контактну особу та місто для клієнта з `CustomerID = 1`:

```sql
UPDATE Customers
SET ContactName = N'Alfred Schmidt', City = N'Frankfurt'
WHERE CustomerID = 1;

SELECT CustomerID, CustomerName, ContactName, City
FROM Customers
WHERE CustomerID = 1;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>ContactName</th><th>City</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td><td>Alfred Schmidt</td><td>Frankfurt</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Оновлення кількох записів

Кількість змінених рядків визначає умова `WHERE`.

<div class="example" markdown="1">

Встановити контактну особу «Juan» для всіх клієнтів з Мексики:

```sql
UPDATE Customers
SET ContactName = N'Juan'
WHERE Country = N'Mexico';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 2</p>
<!-- run:end -->

</div>

## Оновлення з використанням виразу

Нове значення можна обчислити на основі поточного:

<div class="example" markdown="1">

Підвищити ціни на всі напої (категорія 1) на 10%:

```sql
UPDATE Products
SET Price = Price * 1.10
WHERE CategoryID = 1;

SELECT ProductName, Price FROM Products WHERE CategoryID = 1;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Chais</td><td>19.80</td></tr>
<tr><td>Chang</td><td>20.90</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Оновлення з JOIN

У T-SQL інструкція `UPDATE` може містити `FROM` і `JOIN`, щоб використати дані з інших таблиць:

<div class="example" markdown="1">

Знизити на 5% ціни товарів постачальників із США:

```sql
UPDATE p
SET p.Price = p.Price * 0.95
FROM Products AS p
INNER JOIN Suppliers AS s ON p.SupplierID = s.SupplierID
WHERE s.Country = N'USA';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 5</p>
<!-- run:end -->

</div>

## Помилка: UPDATE без WHERE

```sql
UPDATE Customers
SET ContactName = N'Juan';
```

Ця інструкція змінить `ContactName` у **всіх** клієнтів.

<div class="note" markdown="1">
**Порада.** Перед виконанням `UPDATE` або `DELETE` спочатку виконайте `SELECT` з тією самою умовою `WHERE` — так ви побачите, які рядки буде змінено. А для важливих змін використовуйте [транзакції](transactions.html).
</div>
