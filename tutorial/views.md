---
title: "Представлення (Views)"
h1: "Представлення (Views)"
---

**Представлення** (view) — це віртуальна таблиця, побудована на основі результату SQL-запиту.

Представлення містить рядки й стовпці, як справжня таблиця. Стовпці представлення — це стовпці однієї або кількох реальних таблиць бази даних.

Представлення не зберігає дані (якщо воно не індексоване) — щоразу при зверненні до нього виконується його запит, тому воно завжди показує актуальні дані.

## Синтаксис CREATE VIEW

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

<div class="note" markdown="1">
`CREATE VIEW` має бути **першою** інструкцією пакета. У SSMS відокремлюйте її від попереднього коду рядком `GO`.
</div>

## Приклад

<div class="example" markdown="1">

Представлення з усіма клієнтами з України:

```sql
CREATE VIEW UkrainianCustomers AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = N'Ukraine';
GO

SELECT * FROM UkrainianCustomers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>ContactName</th><th>City</th></tr>
<tr><td>Kyiv Market</td><td>Olena Shevchenko</td><td>Kyiv</td></tr>
<tr><td>Lviv Coffee House</td><td>Taras Kovalenko</td><td>Lviv</td></tr>
<tr><td>Odesa Seafood</td><td><span class="null">NULL</span></td><td>Odesa</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Представлення з товарами, дорожчими за середню ціну:

```sql
CREATE VIEW ProductsAboveAveragePrice AS
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
GO

SELECT * FROM ProductsAboveAveragePrice;
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

## Представлення з кількох таблиць

<div class="example" markdown="1">

```sql
CREATE VIEW OrderTotals AS
SELECT o.OrderID, c.CustomerName, o.OrderDate,
       SUM(od.Quantity * p.Price) AS Total
FROM Orders AS o
JOIN Customers    AS c  ON c.CustomerID = o.CustomerID
JOIN OrderDetails AS od ON od.OrderID   = o.OrderID
JOIN Products     AS p  ON p.ProductID  = od.ProductID
GROUP BY o.OrderID, c.CustomerName, o.OrderDate;
GO

SELECT TOP (5) * FROM OrderTotals ORDER BY Total DESC;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerName</th><th>OrderDate</th><th>Total</th></tr>
<tr><td>10253</td><td>Around the Horn</td><td>2024-07-10</td><td>2120.00</td></tr>
<tr><td>10255</td><td>Bólido Comidas preparadas</td><td>2024-07-12</td><td>1652.25</td></tr>
<tr><td>10248</td><td>Around the Horn</td><td>2024-07-04</td><td>1441.50</td></tr>
<tr><td>10250</td><td>Antonio Moreno Taquería</td><td>2024-07-08</td><td>1310.00</td></tr>
<tr><td>10257</td><td>Kyiv Market</td><td>2024-09-01</td><td>1032.00</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
У представленні не можна використовувати `ORDER BY` (крім випадку з `TOP` або `OFFSET`). Сортуйте результат у запиті, який звертається до представлення.
</div>

## Зміна представлення: ALTER VIEW

```sql
ALTER VIEW UkrainianCustomers AS
SELECT CustomerName, ContactName, City, Address
FROM Customers
WHERE Country = N'Ukraine';
```

Починаючи з SQL Server 2016 SP1 є зручна форма, яка створює представлення або змінює наявне:

```sql
CREATE OR ALTER VIEW UkrainianCustomers AS
SELECT CustomerName, City
FROM Customers
WHERE Country = N'Ukraine';
```

## Видалення представлення: DROP VIEW

```sql
DROP VIEW UkrainianCustomers;

-- або
DROP VIEW IF EXISTS UkrainianCustomers;
```

## Навіщо потрібні представлення?

* **Спрощення** — складний запит з кількома JOIN «ховається» за простим ім'ям.
* **Безпека** — користувачам можна дати доступ до представлення, але не до таблиць (наприклад, без стовпця із зарплатою).
* **Стабільний інтерфейс** — структуру таблиць можна змінювати, а представлення залишати незмінним для застосунків.

## Зміна даних через представлення

Через просте представлення (на основі однієї таблиці, без агрегатів, `DISTINCT` та `GROUP BY`) можна виконувати `INSERT`, `UPDATE` і `DELETE`. Опція `WITH CHECK OPTION` забороняє зміни, після яких рядок «випаде» з представлення:

```sql
CREATE VIEW CheapProducts AS
SELECT ProductID, ProductName, Price
FROM Products
WHERE Price < 20
WITH CHECK OPTION;
```
