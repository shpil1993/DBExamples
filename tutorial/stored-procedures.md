---
title: "Збережені процедури"
h1: "Збережені процедури (Stored Procedures)"
---

**Збережена процедура** — це підготовлений код T-SQL, збережений у базі даних під певним ім'ям, який можна викликати багато разів.

Якщо ви часто виконуєте один і той самий запит, збережіть його як процедуру і просто викликайте її. Процедурі можна передавати параметри.

Переваги збережених процедур:

* повторне використання коду;
* безпека: користувачу можна дати право лише на виконання процедури, без доступу до таблиць;
* захист від [SQL-ін'єкцій](sql-injection.html) завдяки параметрам;
* менше мережевого трафіку — на сервер передається лише ім'я процедури та параметри.

## Синтаксис

```sql
CREATE PROCEDURE procedure_name
AS
BEGIN
    sql_statement
END;
```

## Виклик процедури

```sql
EXEC procedure_name;
```

## Процедура без параметрів

<div class="example" markdown="1">

```sql
CREATE PROCEDURE SelectAllCustomers
AS
BEGIN
    SELECT CustomerID, CustomerName, Country FROM Customers;
END;
GO

EXEC SelectAllCustomers;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>Country</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td><td>Germany</td></tr>
<tr><td>2</td><td>Ana Trujillo Emparedados y helados</td><td>Mexico</td></tr>
<tr><td>3</td><td>Antonio Moreno Taquería</td><td>Mexico</td></tr>
</table></div>
<p class="result-more">… показано 3 з 13 рядків</p>
<!-- run:end -->

</div>

## Процедура з одним параметром

<div class="example" markdown="1">

Клієнти з певного міста:

```sql
CREATE PROCEDURE SelectCustomersByCity
    @City NVARCHAR(50)
AS
BEGIN
    SELECT CustomerName, City FROM Customers WHERE City = @City;
END;
GO

EXEC SelectCustomersByCity @City = N'México D.F.';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>México D.F.</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>México D.F.</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Процедура з кількома параметрами

<div class="example" markdown="1">

```sql
CREATE PROCEDURE SelectCustomers
    @City       NVARCHAR(50),
    @PostalCode NVARCHAR(20)
AS
BEGIN
    SELECT CustomerName, City, PostalCode
    FROM Customers
    WHERE City = @City AND PostalCode = @PostalCode;
END;
GO

EXEC SelectCustomers @City = N'London', @PostalCode = N'WA1 1DP';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th><th>PostalCode</th></tr>
<tr><td>Around the Horn</td><td>London</td><td>WA1 1DP</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Параметри можна передавати за іменем (`@City = ...`) або за позицією: `EXEC SelectCustomers N'London', N'WA1 1DP';`. Передача за іменем зрозуміліша й надійніша.

## Значення за замовчуванням

<div class="example" markdown="1">

```sql
CREATE PROCEDURE ProductsByPrice
    @MinPrice DECIMAL(10,2) = 0,
    @MaxPrice DECIMAL(10,2) = 1000000
AS
BEGIN
    SET NOCOUNT ON;
    SELECT ProductName, Price
    FROM Products
    WHERE Price BETWEEN @MinPrice AND @MaxPrice
    ORDER BY Price;
END;
GO

EXEC ProductsByPrice @MinPrice = 30;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Uncle Bob's Organic Dried Pears</td><td>30.00</td></tr>
<tr><td>Ikura</td><td>31.00</td></tr>
<tr><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>40.00</td></tr>
<tr><td>Vegie-spread</td><td>43.90</td></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

`SET NOCOUNT ON` вимикає повідомлення «(N rows affected)» — це трохи пришвидшує роботу процедур, і так прийнято писати.

## Вихідні параметри (OUTPUT)

<div class="example" markdown="1">

```sql
CREATE PROCEDURE GetCustomerOrderCount
    @CustomerID INT,
    @OrderCount INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT @OrderCount = COUNT(*) FROM Orders WHERE CustomerID = @CustomerID;
END;
GO

DECLARE @cnt INT;
EXEC GetCustomerOrderCount @CustomerID = 4, @OrderCount = @cnt OUTPUT;
SELECT @cnt AS OrdersOfCustomer4;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrdersOfCustomer4</th></tr>
<tr><td>2</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Код повернення (RETURN)

```sql
CREATE PROCEDURE CheckCountry
    @Country NVARCHAR(50)
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Customers WHERE Country = @Country)
        RETURN 1;
    RETURN 0;
END;
GO

DECLARE @rc INT;
EXEC @rc = CheckCountry @Country = N'Ukraine';
SELECT @rc AS ReturnCode;
```

## Зміна та видалення процедури

```sql
-- Змінити (або створити, якщо немає) — SQL Server 2016 SP1+
CREATE OR ALTER PROCEDURE SelectAllCustomers
AS
BEGIN
    SELECT * FROM Customers ORDER BY CustomerName;
END;
GO

-- Видалити
DROP PROCEDURE IF EXISTS SelectAllCustomers;
```

## Перегляд процедур

```sql
SELECT name, create_date, modify_date
FROM sys.procedures;

-- Текст процедури
EXEC sp_helptext 'SelectCustomersByCity';
```

<div class="note" markdown="1">
Не називайте власні процедури з префіксом `sp_` — він зарезервований для системних процедур, і SQL Server спершу шукатиме таку процедуру в базі `master`.
</div>
