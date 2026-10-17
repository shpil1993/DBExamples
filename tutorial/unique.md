---
title: "UNIQUE"
h1: "Обмеження UNIQUE"
---

Обмеження `UNIQUE** гарантує, що всі значення в стовпці (або комбінації стовпців) **різні**.

* І `UNIQUE`, і `PRIMARY KEY` гарантують унікальність.
* `PRIMARY KEY` автоматично є унікальним.
* У таблиці може бути **багато** обмежень `UNIQUE`, але лише **один** `PRIMARY KEY`.

## UNIQUE у CREATE TABLE

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL UNIQUE,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    Age       INT
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

Щоб задати ім'я обмеженню або зробити його для кількох стовпців:

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    Age       INT,
    CONSTRAINT UC_Person UNIQUE (ID, LastName)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## UNIQUE в ALTER TABLE

```sql
ALTER TABLE Persons
ADD UNIQUE (ID);
```

Іменоване обмеження для кількох стовпців:

<div class="example" markdown="1">

```sql
ALTER TABLE Suppliers
ADD CONSTRAINT UQ_Suppliers_Name UNIQUE (SupplierName);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## Видалення обмеження UNIQUE

```sql
ALTER TABLE Persons
DROP CONSTRAINT UC_Person;
```

## Порушення UNIQUE

<div class="example" markdown="1">

```sql
ALTER TABLE Shippers
ADD CONSTRAINT UQ_Shippers_Name UNIQUE (ShipperName);

INSERT INTO Shippers (ShipperName) VALUES (N'Speedy Express');
```

</div>

```text
Violation of UNIQUE KEY constraint 'UQ_Shippers_Name'.
Cannot insert duplicate key in object 'dbo.Shippers'. The duplicate key value is (Speedy Express).
```

<div class="note" markdown="1">
**Особливість SQL Server.** Звичайне обмеження `UNIQUE` дозволяє лише **одне** значення `NULL` у стовпці (у MySQL і PostgreSQL — скільки завгодно). Якщо потрібна унікальність лише серед не-NULL значень, створіть фільтрований унікальний індекс:

```sql
CREATE UNIQUE INDEX UX_Customers_Email
ON Customers (Email)
WHERE Email IS NOT NULL;
```
</div>
