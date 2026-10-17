---
title: "PRIMARY KEY"
h1: "Обмеження PRIMARY KEY"
---

Обмеження `PRIMARY KEY` (первинний ключ) однозначно ідентифікує кожен рядок таблиці.

* Значення первинного ключа мають бути **унікальними**.
* Первинний ключ **не може** містити `NULL`.
* Таблиця може мати лише **один** первинний ключ, який може складатися з одного або кількох стовпців (складений ключ).

## PRIMARY KEY у CREATE TABLE

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL PRIMARY KEY,
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

Іменований і складений первинний ключ:

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    Age       INT,
    CONSTRAINT PK_Person PRIMARY KEY (ID, LastName)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
У цьому прикладі є лише **один** первинний ключ — `PK_Person`, але його значення складається з двох стовпців (`ID` + `LastName`).
</div>

## PRIMARY KEY в ALTER TABLE

Стовпці первинного ключа мають бути оголошені як `NOT NULL`.

```sql
ALTER TABLE Persons
ADD PRIMARY KEY (ID);
```

```sql
ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID, LastName);
```

## Видалення PRIMARY KEY

```sql
ALTER TABLE Persons
DROP CONSTRAINT PK_Person;
```

## Первинний ключ і кластерний індекс

У SQL Server первинний ключ за замовчуванням створює **кластерний індекс** — дані таблиці фізично впорядковуються за значенням ключа. Тому вдалий первинний ключ:

* короткий (наприклад, `INT` або `BIGINT`);
* незмінний;
* бажано, щоб зростав (як `IDENTITY`).

Якщо потрібно, ключ можна зробити некластерним:

```sql
CREATE TABLE Sessions (
    SessionID UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),
    CreatedAt DATETIME2 NOT NULL,
    CONSTRAINT PK_Sessions PRIMARY KEY NONCLUSTERED (SessionID)
);
```

## Автоматичний первинний ключ

Найчастіше первинний ключ поєднують з властивістю `IDENTITY`, щоб сервер сам генерував значення:

```sql
CREATE TABLE Products2 (
    ProductID   INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL
);
```

Детальніше — в уроці [IDENTITY](identity.html).
