---
title: "CHECK"
h1: "Обмеження CHECK"
---

Обмеження `CHECK` обмежує діапазон значень, які можна записати в стовпець.

* `CHECK` на стовпці дозволяє лише певні значення для цього стовпця.
* `CHECK` на таблиці може обмежувати значення стовпців на основі інших стовпців того ж рядка.

## CHECK у CREATE TABLE

<div class="example" markdown="1">

Вік особи має бути не меншим за 18:

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    Age       INT CHECK (Age >= 18)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

Іменоване обмеження для кількох стовпців:

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    Age       INT,
    City      NVARCHAR(255),
    CONSTRAINT CHK_Person CHECK (Age >= 18 AND City = N'Kyiv')
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## Порівняння двох стовпців

<div class="example" markdown="1">

Дата завершення не може бути раніше за дату початку:

```sql
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    StartDate DATE NOT NULL,
    EndDate   DATE NULL,
    CONSTRAINT CK_Projects_Dates CHECK (EndDate IS NULL OR EndDate >= StartDate)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## CHECK в ALTER TABLE

```sql
ALTER TABLE Persons
ADD CHECK (Age >= 18);
```

<div class="example" markdown="1">

Ціна товару не може бути від'ємною:

```sql
ALTER TABLE Products
ADD CONSTRAINT CK_Products_Price CHECK (Price >= 0);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## Порушення CHECK

<div class="example" markdown="1">

```sql
ALTER TABLE Products
ADD CONSTRAINT CK_Products_Price CHECK (Price >= 0);

UPDATE Products SET Price = -5 WHERE ProductID = 1;
```

</div>

```text
The UPDATE statement conflicted with the CHECK constraint "CK_Products_Price".
```

## Видалення CHECK

```sql
ALTER TABLE Persons
DROP CONSTRAINT CHK_Person;
```

<div class="note" markdown="1">
Умова `CHECK` вважається виконаною, якщо її результат — `TRUE` **або** `UNKNOWN`. Тому `NULL` у стовпці `Age` пройде перевірку `Age >= 18`. Щоб заборонити `NULL`, додайте ще й `NOT NULL`.
</div>
