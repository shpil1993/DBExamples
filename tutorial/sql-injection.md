---
title: "SQL-ін'єкції"
h1: "SQL-ін'єкції"
---

**SQL-ін'єкція** — це техніка атаки, за якої зловмисник вставляє фрагмент SQL-коду у введені дані, а застосунок без перевірки підставляє їх у запит.

SQL-ін'єкції — одна з найпоширеніших вразливостей вебзастосунків. Вони можуть призвести до витоку, зміни або знищення даних.

## Як виникає ін'єкція

Ін'єкція можлива, коли запит **склеюється з рядків**, а частина рядка надходить від користувача. Наприклад, код застосунку (C#):

```csharp
string userId = Request.Query["UserId"];
string sql = "SELECT * FROM Users WHERE UserId = " + userId;
```

Якщо користувач введе `105`, запит буде нормальним:

```sql
SELECT * FROM Users WHERE UserId = 105;
```

## Ін'єкція «1=1 завжди істинне»

Якщо ж користувач введе `105 OR 1=1`, запит стане таким:

```sql
SELECT * FROM Users WHERE UserId = 105 OR 1=1;
```

Умова `1=1` завжди істинна, тож запит поверне **всіх** користувачів — разом з їхніми логінами та паролями.

## Ін'єкція «""="" завжди істинне»

Форма входу на сайт:

```csharp
string sql = "SELECT * FROM Users WHERE Name = '" + userName +
             "' AND Pass = '" + userPass + "'";
```

Якщо в обидва поля ввести `' OR ''='`, отримаємо:

```sql
SELECT * FROM Users WHERE Name = '' OR ''='' AND Pass = '' OR ''='';
```

Умова завжди істинна — зловмисник увійде без пароля.

## Пакетні інструкції

SQL Server дозволяє виконувати кілька інструкцій в одному запиті. Якщо користувач введе

```text
105; DROP TABLE Suppliers
```

то запит буде таким:

```sql
SELECT * FROM Users WHERE UserId = 105; DROP TABLE Suppliers;
```

## Захист: параметризовані запити

Єдиний надійний спосіб захисту — **ніколи не склеювати SQL з даними користувача**. Використовуйте **параметри**: значення передаються на сервер окремо від тексту запиту і ніколи не виконуються як код.

**C# (ADO.NET):**

```csharp
using var cmd = new SqlCommand(
    "SELECT * FROM Customers WHERE CustomerID = @id", connection);
cmd.Parameters.Add("@id", SqlDbType.Int).Value = customerId;
using var reader = cmd.ExecuteReader();
```

**Python (pyodbc):**

```python
cursor.execute("SELECT * FROM Customers WHERE City = ?", city)
```

## Динамічний SQL у T-SQL: sp_executesql

Якщо текст запиту формується всередині T-SQL, використовуйте `sp_executesql` з параметрами, а не `EXEC` зі склеєним рядком.

<div class="example" markdown="1">

**Небезпечно:**

```sql
DECLARE @city NVARCHAR(50) = N'Berlin''; DROP TABLE Suppliers; --';
DECLARE @sql  NVARCHAR(MAX) = N'SELECT * FROM Customers WHERE City = ''' + @city + N'''';
-- EXEC (@sql);   -- виконало б і DROP TABLE!
PRINT @sql;
```

</div>

<div class="example" markdown="1">

**Безпечно:**

```sql
DECLARE @city NVARCHAR(50) = N'Berlin';

EXEC sp_executesql
    N'SELECT CustomerName, City FROM Customers WHERE City = @c',
    N'@c NVARCHAR(50)',
    @c = @city;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Berlin</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Якщо потрібно підставити в динамічний SQL **ім'я** об'єкта (таблиці, стовпця), яке не можна передати параметром, використовуйте функцію `QUOTENAME()`:

```sql
DECLARE @table SYSNAME = N'Customers';
DECLARE @sql NVARCHAR(MAX) = N'SELECT COUNT(*) FROM dbo.' + QUOTENAME(@table);
EXEC sp_executesql @sql;
```

## Інші заходи захисту

* **Мінімальні права** — обліковий запис застосунку не повинен мати прав на `DROP` чи доступ до зайвих таблиць.
* **Збережені процедури** з параметрами замість довільних запитів.
* **Перевірка введення** (тип, довжина, формат) — додатковий, але не єдиний захід.
* **ORM-бібліотеки** (Entity Framework, Dapper) за замовчуванням використовують параметри.
