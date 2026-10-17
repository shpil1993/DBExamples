---
title: "EXISTS"
h1: "Оператор EXISTS"
---

Оператор `EXISTS` перевіряє, чи повертає підзапит **хоча б один рядок**.

`EXISTS` повертає `TRUE`, якщо підзапит повертає один або більше рядків.

## Синтаксис

```sql
SELECT column_name(s)
FROM table_name
WHERE EXISTS
    (SELECT column_name FROM table_name WHERE condition);
```

## Приклад

<div class="example" markdown="1">

Постачальники, у яких є товар дешевший за 20:

```sql
SELECT s.SupplierName
FROM Suppliers AS s
WHERE EXISTS (
    SELECT 1 FROM Products AS p
    WHERE p.SupplierID = s.SupplierID AND p.Price < 20
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>SupplierName</th></tr>
<tr><td>Exotic Liquid</td></tr>
<tr><td>Pavlova, Ltd.</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

Підзапит тут **корельований**: він посилається на зовнішню таблицю (`s.SupplierID`) і логічно виконується для кожного постачальника.

<div class="note" markdown="1">
Що саме вибирає підзапит у `EXISTS` — неважливо: важлива лише наявність рядків. Тому часто пишуть `SELECT 1` або `SELECT *`.
</div>

<div class="example" markdown="1">

Постачальники, у яких є товар з ціною рівно 22:

```sql
SELECT s.SupplierName
FROM Suppliers AS s
WHERE EXISTS (
    SELECT 1 FROM Products AS p
    WHERE p.SupplierID = s.SupplierID AND p.Price = 22
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>SupplierName</th></tr>
<tr><td>New Orleans Cajun Delights</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## NOT EXISTS

<div class="example" markdown="1">

Клієнти, у яких немає жодного замовлення:

```sql
SELECT c.CustomerName
FROM Customers AS c
WHERE NOT EXISTS (
    SELECT 1 FROM Orders AS o
    WHERE o.CustomerID = c.CustomerID
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Blauer See Delikatessen</td></tr>
<tr><td>Odesa Seafood</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

`NOT EXISTS` — надійна альтернатива `NOT IN`: вона коректно працює, навіть якщо в підзапиті трапляються значення `NULL`.

## IF EXISTS

У T-SQL `EXISTS` часто використовують в умовах `IF`:

```sql
IF EXISTS (SELECT 1 FROM Customers WHERE Country = N'Ukraine')
    PRINT N'Є клієнти з України';
ELSE
    PRINT N'Клієнтів з України немає';
```
