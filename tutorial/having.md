---
title: "HAVING"
h1: "Умова HAVING"
---

Умова `HAVING` з'явилася в SQL тому, що в `WHERE` **не можна** використовувати агрегатні функції.

* `WHERE` фільтрує **рядки** до групування;
* `HAVING` фільтрує **групи** після групування.

## Синтаксис

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

## Приклад

<div class="example" markdown="1">

Країни, у яких більше одного клієнта:

```sql
SELECT Country, COUNT(CustomerID) AS Customers
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 1;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th><th>Customers</th></tr>
<tr><td>France</td><td>2</td></tr>
<tr><td>Germany</td><td>2</td></tr>
<tr><td>Mexico</td><td>2</td></tr>
<tr><td>Ukraine</td><td>3</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Те саме, відсортоване за кількістю:

```sql
SELECT Country, COUNT(CustomerID) AS Customers
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 1
ORDER BY COUNT(CustomerID) DESC;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th><th>Customers</th></tr>
<tr><td>Ukraine</td><td>3</td></tr>
<tr><td>France</td><td>2</td></tr>
<tr><td>Germany</td><td>2</td></tr>
<tr><td>Mexico</td><td>2</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>

## HAVING з JOIN

<div class="example" markdown="1">

Працівники, які оформили більше двох замовлень:

```sql
SELECT e.LastName, COUNT(o.OrderID) AS NumberOfOrders
FROM Orders AS o
INNER JOIN Employees AS e ON o.EmployeeID = e.EmployeeID
GROUP BY e.LastName
HAVING COUNT(o.OrderID) > 2;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>LastName</th><th>NumberOfOrders</th></tr>
<tr><td>Davolio</td><td>3</td></tr>
<tr><td>Leverling</td><td>3</td></tr>
<tr><td>Peacock</td><td>4</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## WHERE і HAVING разом

<div class="example" markdown="1">

Чи оформили працівники «Davolio» або «Peacock» більше двох замовлень:

```sql
SELECT e.LastName, COUNT(o.OrderID) AS NumberOfOrders
FROM Orders AS o
INNER JOIN Employees AS e ON o.EmployeeID = e.EmployeeID
WHERE e.LastName IN (N'Davolio', N'Peacock')
GROUP BY e.LastName
HAVING COUNT(o.OrderID) > 2;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>LastName</th><th>NumberOfOrders</th></tr>
<tr><td>Davolio</td><td>3</td></tr>
<tr><td>Peacock</td><td>4</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Порядок виконання запиту

Логічно SQL Server обробляє частини запиту в такому порядку:

1. `FROM` і `JOIN`
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `ORDER BY`
7. `TOP` / `OFFSET ... FETCH`

Саме тому в `WHERE` не можна використовувати агрегати, а псевдоніми з `SELECT` доступні лише в `ORDER BY`.
