---
title: "COUNT(), AVG(), SUM()"
h1: Функції COUNT(), AVG() та SUM()
---

* `COUNT()` повертає **кількість** рядків, що відповідають умові.
* `AVG()` повертає **середнє** значення числового стовпця.
* `SUM()` повертає **суму** значень числового стовпця.

## Синтаксис

```sql
SELECT COUNT(column_name) FROM table_name WHERE condition;

SELECT AVG(column_name) FROM table_name WHERE condition;

SELECT SUM(column_name) FROM table_name WHERE condition;
```

## COUNT()

<div class="example" markdown="1">

Порахувати кількість товарів:

```sql
SELECT COUNT(*) AS ProductCount
FROM Products;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductCount</th></tr>
<tr><td>15</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

### COUNT(*) проти COUNT(column)

* `COUNT(*)` рахує **всі рядки**.
* `COUNT(column)` рахує лише рядки, де значення стовпця **не NULL**.
* `COUNT(DISTINCT column)` рахує **різні** значення, які не є NULL.

<div class="example" markdown="1">

```sql
SELECT
    COUNT(*)                   AS AllCustomers,
    COUNT(ContactName)         AS WithContact,
    COUNT(DISTINCT Country)    AS Countries
FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>AllCustomers</th><th>WithContact</th><th>Countries</th></tr>
<tr><td>13</td><td>12</td><td>8</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
`COUNT()` повертає тип `INT`. Для дуже великих таблиць (понад 2 мільярди рядків) використовуйте `COUNT_BIG()`, яка повертає `BIGINT`.
</div>

## AVG()

<div class="example" markdown="1">

Середня ціна товарів:

```sql
SELECT AVG(Price) AS AveragePrice
FROM Products;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>AveragePrice</th></tr>
<tr><td>29.513333</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
**Увага: цілочисельне ділення.** Якщо стовпець має цілий тип (`INT`), `AVG()` теж поверне ціле число, відкинувши дробову частину:

```sql
SELECT AVG(Quantity) AS AvgInt,
       AVG(CAST(Quantity AS DECIMAL(10,2))) AS AvgDecimal
FROM OrderDetails;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>AvgInt</th><th>AvgDecimal</th></tr>
<tr><td>18</td><td>18.592592</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Знайти товари, дорожчі за середню ціну:

<div class="example" markdown="1">

```sql
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Uncle Bob's Organic Dried Pears</td><td>30.00</td></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>40.00</td></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>Ikura</td><td>31.00</td></tr>
<tr><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
<tr><td>Vegie-spread</td><td>43.90</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

## SUM()

<div class="example" markdown="1">

Загальна кількість проданих одиниць товару:

```sql
SELECT SUM(Quantity) AS TotalQuantity
FROM OrderDetails;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>TotalQuantity</th></tr>
<tr><td>502</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

### SUM() з виразом

У `SUM()` можна передати вираз. Наприклад, обчислимо загальну вартість усіх замовлень:

<div class="example" markdown="1">

```sql
SELECT SUM(od.Quantity * p.Price) AS TotalRevenue
FROM OrderDetails AS od
JOIN Products AS p ON od.ProductID = p.ProductID;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>TotalRevenue</th></tr>
<tr><td>12458.25</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Агрегати з умовою WHERE

<div class="example" markdown="1">

Кількість і сума одиниць у замовленні 10248:

```sql
SELECT COUNT(*) AS Lines, SUM(Quantity) AS Units
FROM OrderDetails
WHERE OrderID = 10248;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Lines</th><th>Units</th></tr>
<tr><td>3</td><td>27</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Щоб отримати агрегати для кожної групи (наприклад, для кожного замовлення), використовуйте [GROUP BY](group-by.html).
