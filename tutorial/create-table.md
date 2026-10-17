---
title: "CREATE TABLE"
h1: "Інструкція CREATE TABLE"
---

Інструкція `CREATE TABLE` створює нову таблицю в базі даних.

## Синтаксис

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);
```

Параметр `datatype` задає тип даних стовпця (наприклад, `INT`, `NVARCHAR`, `DATE`). Повний перелік типів — у довіднику [Типи даних](data-types.html).

## Приклад

<div class="example" markdown="1">

Створити таблицю `Persons` з п'ятьма стовпцями:

```sql
CREATE TABLE Persons (
    PersonID  INT,
    LastName  NVARCHAR(255),
    FirstName NVARCHAR(255),
    Address   NVARCHAR(255),
    City      NVARCHAR(255)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

* `PersonID` має тип `INT` і зберігає ціле число.
* Стовпці `LastName`, `FirstName`, `Address` і `City` мають тип `NVARCHAR(255)` — текст Unicode довжиною до 255 символів.

Нова таблиця поки що порожня. Заповнити її можна інструкцією [INSERT INTO](insert.html).

## Таблиця з ключем та обмеженнями

На практиці таблиці майже завжди мають первинний ключ та інші обмеження:

<div class="example" markdown="1">

```sql
CREATE TABLE dbo.Students (
    StudentID  INT IDENTITY(1,1) PRIMARY KEY,
    FirstName  NVARCHAR(50)  NOT NULL,
    LastName   NVARCHAR(50)  NOT NULL,
    Email      NVARCHAR(100) UNIQUE,
    BirthDate  DATE,
    Scholarship DECIMAL(8,2) DEFAULT 0 CHECK (Scholarship >= 0),
    CreatedAt  DATETIME2     NOT NULL DEFAULT SYSDATETIME()
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

Детальніше про `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK` — у розділі [Обмеження](constraints.html), а про `IDENTITY` — в уроці [IDENTITY](identity.html).

## Створення таблиці на основі іншої

У SQL Server нову таблицю з даними іншої таблиці створюють за допомогою [SELECT INTO](select-into.html):

<div class="example" markdown="1">

```sql
SELECT CustomerName, ContactName
INTO TestTable
FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 13</p>
<!-- run:end -->

</div>

## Створення, якщо таблиці ще немає

```sql
IF OBJECT_ID(N'dbo.Persons', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.Persons (
        PersonID INT,
        LastName NVARCHAR(255)
    );
END
```

Функція `OBJECT_ID()` повертає ідентифікатор об'єкта або `NULL`, якщо об'єкта немає. Параметр `'U'` означає «таблиця користувача».

## Перегляд структури таблиці

```sql
EXEC sp_help 'dbo.Persons';

-- або
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Persons';
```
