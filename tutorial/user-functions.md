---
title: "Функції користувача"
h1: "Функції користувача (UDF)"
---

Окрім вбудованих функцій, у SQL Server можна створювати **власні функції** (User-Defined Functions, UDF).

На відміну від збережених процедур, функції:

* **завжди повертають** значення (скалярне або таблицю);
* можуть використовуватися прямо в запитах (`SELECT`, `WHERE`, `JOIN`);
* **не можуть** змінювати дані в таблицях (`INSERT`, `UPDATE`, `DELETE` для постійних таблиць заборонені).

## Скалярна функція

Повертає одне значення.

```sql
CREATE FUNCTION schema.function_name (@param datatype, ...)
RETURNS datatype
AS
BEGIN
    ...
    RETURN value;
END;
```

<div class="example" markdown="1">

Функція, що повертає ціну з ПДВ:

```sql
CREATE FUNCTION dbo.PriceWithVAT (@Price DECIMAL(10,2), @Rate DECIMAL(5,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN @Price * (1 + @Rate / 100);
END;
GO

SELECT ProductName, Price, dbo.PriceWithVAT(Price, 20) AS WithVAT
FROM Products
WHERE CategoryID = 1;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th><th>WithVAT</th></tr>
<tr><td>Chais</td><td>18.00</td><td>21.60</td></tr>
<tr><td>Chang</td><td>19.00</td><td>22.80</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Під час виклику скалярної функції обов'язково вказуйте схему: `dbo.PriceWithVAT(...)`, а не просто `PriceWithVAT(...)`.
</div>

<div class="example" markdown="1">

Функція з логікою — повне ім'я працівника:

```sql
CREATE FUNCTION dbo.FullName (@EmployeeID INT)
RETURNS NVARCHAR(101)
AS
BEGIN
    DECLARE @Name NVARCHAR(101);
    SELECT @Name = FirstName + N' ' + LastName
    FROM Employees WHERE EmployeeID = @EmployeeID;
    RETURN ISNULL(@Name, N'(не вказано)');
END;
GO

SELECT OrderID, dbo.FullName(EmployeeID) AS Employee
FROM Orders
WHERE OrderID >= 10259;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>Employee</th></tr>
<tr><td>10259</td><td>Robert King</td></tr>
<tr><td>10260</td><td>Nancy Davolio</td></tr>
<tr><td>10261</td><td>(не вказано)</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## Вбудована таблична функція (inline TVF)

Повертає таблицю — результат одного запиту `SELECT`. Це як «представлення з параметрами».

<div class="example" markdown="1">

```sql
CREATE FUNCTION dbo.CustomersByCountry (@Country NVARCHAR(50))
RETURNS TABLE
AS
RETURN (
    SELECT CustomerID, CustomerName, City
    FROM Customers
    WHERE Country = @Country
);
GO

SELECT * FROM dbo.CustomersByCountry(N'France');
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>City</th></tr>
<tr><td>7</td><td>Blondel père et fils</td><td>Strasbourg</td></tr>
<tr><td>9</td><td>Bon app'</td><td>Marseille</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

Табличні функції можна використовувати у `FROM` та в `JOIN`, а також з `CROSS APPLY`:

<div class="example" markdown="1">

```sql
CREATE FUNCTION dbo.TopProductsInCategory (@CategoryID INT, @N INT)
RETURNS TABLE
AS
RETURN (
    SELECT TOP (@N) ProductName, Price
    FROM Products
    WHERE CategoryID = @CategoryID
    ORDER BY Price DESC
);
GO

SELECT c.CategoryName, t.ProductName, t.Price
FROM Categories AS c
CROSS APPLY dbo.TopProductsInCategory(c.CategoryID, 1) AS t;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CategoryName</th><th>ProductName</th><th>Price</th></tr>
<tr><td>Beverages</td><td>Chang</td><td>19.00</td></tr>
<tr><td>Condiments</td><td>Vegie-spread</td><td>43.90</td></tr>
<tr><td>Confections</td><td>Pavlova</td><td>17.45</td></tr>
<tr><td>Dairy Products</td><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
<tr><td>Grains/Cereals</td><td>Tunnbröd</td><td>9.00</td></tr>
<tr><td>Meat/Poultry</td><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>Produce</td><td>Uncle Bob's Organic Dried Pears</td><td>30.00</td></tr>
<tr><td>Seafood</td><td>Ikura</td><td>31.00</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

## Багатоінструкційна таблична функція (multi-statement TVF)

Таблицю-результат заповнюють кількома інструкціями:

```sql
CREATE FUNCTION dbo.PriceLevels ()
RETURNS @Result TABLE (Level NVARCHAR(20), ProductCount INT)
AS
BEGIN
    INSERT INTO @Result
    SELECT N'Дешеві', COUNT(*) FROM Products WHERE Price < 20;

    INSERT INTO @Result
    SELECT N'Дорогі', COUNT(*) FROM Products WHERE Price >= 20;

    RETURN;
END;
GO

SELECT * FROM dbo.PriceLevels();
```

<div class="note" markdown="1">
Вбудовані (inline) табличні функції зазвичай працюють значно швидше за багатоінструкційні, бо оптимізатор «розгортає» їх у запит, як представлення.
</div>

## Зміна та видалення функції

```sql
CREATE OR ALTER FUNCTION dbo.PriceWithVAT (@Price DECIMAL(10,2), @Rate DECIMAL(5,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN ROUND(@Price * (1 + @Rate / 100), 2);
END;
GO

DROP FUNCTION IF EXISTS dbo.PriceWithVAT;
```
