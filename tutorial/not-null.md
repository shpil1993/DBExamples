---
title: "NOT NULL"
h1: "Обмеження NOT NULL"
---

За замовчуванням стовпець може містити значення `NULL`.

Обмеження `NOT NULL` забороняє стовпцю приймати `NULL`. Тобто поле завжди повинно мати значення: не можна додати запис або оновити його, не вказавши значення цього поля.

## NOT NULL у CREATE TABLE

<div class="example" markdown="1">

Стовпці `ID`, `LastName` і `FirstName` не прийматимуть значення `NULL`:

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255) NOT NULL,
    Age       INT
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## Спроба вставити NULL

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    ID       INT NOT NULL,
    LastName NVARCHAR(255) NOT NULL
);

INSERT INTO Persons (ID) VALUES (1);
```

</div>

SQL Server поверне помилку:

```text
Cannot insert the value NULL into column 'LastName', table 'DemoShop.dbo.Persons';
column does not allow nulls. INSERT fails.
```

## NOT NULL в ALTER TABLE

Щоб додати `NOT NULL` до існуючого стовпця, використовуйте `ALTER COLUMN` (тип даних потрібно вказати повторно):

<div class="example" markdown="1">

```sql
ALTER TABLE Customers
ALTER COLUMN Country NVARCHAR(50) NOT NULL;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
Якщо в стовпці вже є значення `NULL`, команда завершиться помилкою. Спочатку оновіть такі рядки, наприклад: `UPDATE Customers SET Country = N'Unknown' WHERE Country IS NULL;`
</div>

## Додавання нового стовпця NOT NULL

Новий стовпець `NOT NULL` у таблиці з даними потребує значення за замовчуванням — інакше чим заповнити існуючі рядки?

<div class="example" markdown="1">

```sql
ALTER TABLE Customers
ADD IsActive BIT NOT NULL DEFAULT 1;
GO

SELECT TOP (3) CustomerName, IsActive FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>IsActive</th></tr>
<tr><td>Alfreds Futterkiste</td><td>1</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>1</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>1</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>
