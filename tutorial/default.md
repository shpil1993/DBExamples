---
title: "DEFAULT"
h1: "Обмеження DEFAULT"
---

Обмеження `DEFAULT` задає **значення за замовчуванням** для стовпця.

Значення за замовчуванням записується в нові рядки, якщо для стовпця не вказано інше значення.

## DEFAULT у CREATE TABLE

<div class="example" markdown="1">

Місто за замовчуванням — «Kyiv»:

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    Age       INT,
    City      NVARCHAR(255) DEFAULT N'Kyiv'
);

INSERT INTO Persons (ID, LastName) VALUES (1, N'Shevchenko');
SELECT * FROM Persons;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ID</th><th>LastName</th><th>FirstName</th><th>Age</th><th>City</th></tr>
<tr><td>1</td><td>Shevchenko</td><td><span class="null">NULL</span></td><td><span class="null">NULL</span></td><td>Kyiv</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

`DEFAULT` можна використовувати й з функціями, наприклад `GETDATE()`:

<div class="example" markdown="1">

```sql
CREATE TABLE Orders2 (
    ID          INT NOT NULL,
    OrderNumber INT NOT NULL,
    OrderDate   DATE DEFAULT GETDATE()
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## DEFAULT в ALTER TABLE

У SQL Server значення за замовчуванням для існуючого стовпця додається як іменоване обмеження з ключовим словом `FOR`:

```sql
ALTER TABLE Persons
ADD CONSTRAINT DF_Persons_City
DEFAULT N'Kyiv' FOR City;
```

<div class="note" markdown="1">
У MySQL для цього використовують `ALTER COLUMN City SET DEFAULT 'Kyiv'`. У SQL Server такий синтаксис **не працює** — лише `ADD CONSTRAINT ... DEFAULT ... FOR ...`.
</div>

## Видалення DEFAULT

```sql
ALTER TABLE Persons
DROP CONSTRAINT DF_Persons_City;
```

Якщо ім'я обмеження не задавали явно, його можна знайти так:

```sql
SELECT name
FROM sys.default_constraints
WHERE parent_object_id = OBJECT_ID(N'dbo.Persons');
```

## Явне використання DEFAULT

Ключове слово `DEFAULT` можна вказати в `INSERT` та `UPDATE`:

```sql
INSERT INTO Persons (ID, LastName, City) VALUES (2, N'Franko', DEFAULT);

UPDATE Persons SET City = DEFAULT WHERE ID = 1;
```
