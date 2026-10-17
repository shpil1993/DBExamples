---
title: GROUP BY
h1: Інструкція GROUP BY
---

`GROUP BY` групує рядки з однаковими значеннями в підсумкові рядки — наприклад, «кількість клієнтів у кожній країні».

`GROUP BY` часто використовують з агрегатними функціями `COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`.

## Синтаксис

```sql
SELECT column_name(s), aggregate_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

## Приклад

<div class="example" markdown="1">

Кількість клієнтів у кожній країні:

```sql
SELECT Country, COUNT(CustomerID) AS Customers
FROM Customers
GROUP BY Country;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th><th>Customers</th></tr>
<tr><td>Canada</td><td>1</td></tr>
<tr><td>France</td><td>2</td></tr>
<tr><td>Germany</td><td>2</td></tr>
<tr><td>Mexico</td><td>2</td></tr>
<tr><td>Spain</td><td>1</td></tr>
<tr><td>Sweden</td><td>1</td></tr>
<tr><td>UK</td><td>1</td></tr>
<tr><td>Ukraine</td><td>3</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Те саме, відсортоване від найбільшої кількості:

```sql
SELECT Country, COUNT(CustomerID) AS Customers
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th><th>Customers</th></tr>
<tr><td>Ukraine</td><td>3</td></tr>
<tr><td>France</td><td>2</td></tr>
<tr><td>Germany</td><td>2</td></tr>
</table></div>
<p class="result-more">… показано 3 з 8 рядків</p>
<!-- run:end -->

</div>

## GROUP BY з JOIN

<div class="example" markdown="1">

Кількість замовлень, відправлених кожною службою доставки:

```sql
SELECT s.ShipperName, COUNT(o.OrderID) AS NumberOfOrders
FROM Orders AS o
LEFT JOIN Shippers AS s ON o.ShipperID = s.ShipperID
GROUP BY s.ShipperName;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ShipperName</th><th>NumberOfOrders</th></tr>
<tr><td>Federal Shipping</td><td>3</td></tr>
<tr><td>Speedy Express</td><td>5</td></tr>
<tr><td>United Package</td><td>6</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Сума кожного замовлення:

```sql
SELECT od.OrderID, SUM(od.Quantity * p.Price) AS OrderTotal
FROM OrderDetails AS od
JOIN Products AS p ON p.ProductID = od.ProductID
GROUP BY od.OrderID
ORDER BY OrderTotal DESC;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>OrderTotal</th></tr>
<tr><td>10253</td><td>2120.00</td></tr>
<tr><td>10255</td><td>1652.25</td></tr>
<tr><td>10248</td><td>1441.50</td></tr>
<tr><td>10250</td><td>1310.00</td></tr>
<tr><td>10257</td><td>1032.00</td></tr>
</table></div>
<p class="result-more">… показано 5 з 14 рядків</p>
<!-- run:end -->

</div>

## Групування за кількома стовпцями

<div class="example" markdown="1">

Кількість замовлень за роком і місяцем:

```sql
SELECT YEAR(OrderDate) AS [Year], MONTH(OrderDate) AS [Month], COUNT(*) AS Orders
FROM Orders
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY [Year], [Month];
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Year</th><th>Month</th><th>Orders</th></tr>
<tr><td>2024</td><td>7</td><td>8</td></tr>
<tr><td>2024</td><td>8</td><td>1</td></tr>
<tr><td>2024</td><td>9</td><td>2</td></tr>
<tr><td>2024</td><td>10</td><td>1</td></tr>
<tr><td>2024</td><td>11</td><td>1</td></tr>
<tr><td>2024</td><td>12</td><td>1</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

## Правило GROUP BY

<div class="warn" markdown="1">
Кожен стовпець у `SELECT`, який **не** є агрегатною функцією, обов'язково має бути в `GROUP BY`. Інакше SQL Server поверне помилку:

```text
Column 'Customers.City' is invalid in the select list because it is not contained
in either an aggregate function or the GROUP BY clause.
```
(На відміну від деяких режимів MySQL, SQL Server суворо дотримується цього правила.)
</div>

## ROLLUP: проміжні підсумки

`GROUP BY ROLLUP(...)` додає рядки з підсумками:

<div class="example" markdown="1">

```sql
SELECT Country, COUNT(*) AS Customers
FROM Customers
GROUP BY ROLLUP(Country);
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th><th>Customers</th></tr>
<tr><td>Canada</td><td>1</td></tr>
<tr><td>France</td><td>2</td></tr>
<tr><td>Germany</td><td>2</td></tr>
<tr><td>Mexico</td><td>2</td></tr>
<tr><td>Spain</td><td>1</td></tr>
<tr><td>Sweden</td><td>1</td></tr>
<tr><td>UK</td><td>1</td></tr>
<tr><td>Ukraine</td><td>3</td></tr>
<tr><td><span class="null">NULL</span></td><td>13</td></tr>
</table></div>
<p class="result-more">Рядків: 9</p>
<!-- run:end -->

</div>

Останній рядок з `Country = NULL` містить загальний підсумок.
