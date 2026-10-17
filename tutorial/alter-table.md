---
title: "ALTER TABLE"
h1: "Інструкція ALTER TABLE"
---

Інструкція `ALTER TABLE` змінює структуру існуючої таблиці: додає, видаляє чи змінює стовпці, а також додає та видаляє обмеження.

## ALTER TABLE — ADD (додати стовпець)

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

<div class="example" markdown="1">

Додати стовпець `Email` до таблиці `Customers`:

```sql
ALTER TABLE Customers
ADD Email NVARCHAR(255);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
На відміну від MySQL, у SQL Server після `ADD` **не пишуть** слово `COLUMN`. Можна додати кілька стовпців одразу: `ADD Col1 INT, Col2 DATE;`
</div>

## ALTER TABLE — DROP COLUMN (видалити стовпець)

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

<div class="example" markdown="1">

Видалити стовпець `PostalCode` з таблиці `Customers`:

```sql
ALTER TABLE Customers
DROP COLUMN PostalCode;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
Якщо на стовпці є обмеження (`DEFAULT`, `CHECK`, `FOREIGN KEY`) або індекс, спочатку потрібно видалити їх, інакше SQL Server поверне помилку.
</div>

## ALTER TABLE — RENAME COLUMN (перейменувати стовпець)

У SQL Server немає `ALTER TABLE ... RENAME COLUMN`. Для перейменування використовується системна процедура `sp_rename`:

```sql
EXEC sp_rename 'table_name.old_name', 'new_name', 'COLUMN';
```

<div class="example" markdown="1">

```sql
EXEC sp_rename 'Customers.ContactName', 'ContactPerson', 'COLUMN';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

Так само перейменовується й сама таблиця: `EXEC sp_rename 'OldTable', 'NewTable';`

## ALTER TABLE — ALTER COLUMN (змінити тип даних)

```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```

<div class="example" markdown="1">

Збільшити довжину стовпця `City` та зробити його обов'язковим:

```sql
ALTER TABLE Customers
ALTER COLUMN City NVARCHAR(100) NOT NULL;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## Повний приклад

Розглянемо таблицю `Persons`:

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    ID        INT NOT NULL,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    City      NVARCHAR(255)
);

-- Додати стовпець з датою народження
ALTER TABLE Persons ADD DateOfBirth DATE;
GO

-- Змінити тип: зберігати дату разом із часом
ALTER TABLE Persons ALTER COLUMN DateOfBirth DATETIME2;
GO

SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Persons';

-- Видалити стовпець
ALTER TABLE Persons DROP COLUMN DateOfBirth;

SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Persons';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>COLUMN_NAME</th><th>DATA_TYPE</th></tr>
<tr><td>ID</td><td>int</td></tr>
<tr><td>LastName</td><td>nvarchar</td></tr>
<tr><td>FirstName</td><td>nvarchar</td></tr>
<tr><td>City</td><td>nvarchar</td></tr>
<tr><td>DateOfBirth</td><td>datetime2</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<div class="table-scroll"><table>
<tr><th>COLUMN_NAME</th><th>DATA_TYPE</th></tr>
<tr><td>ID</td><td>int</td></tr>
<tr><td>LastName</td><td>nvarchar</td></tr>
<tr><td>FirstName</td><td>nvarchar</td></tr>
<tr><td>City</td><td>nvarchar</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
`GO` — це не команда T-SQL, а роздільник **пакетів** (batches) для SSMS і sqlcmd. Він потрібен, бо SQL Server компілює пакет цілком: стовпець, доданий у пакеті, ще «не існує» для інших інструкцій того самого пакета. Детальніше — в уроці [Змінні та пакети](variables.html).
</div>

## Додавання та видалення обмежень

```sql
-- Додати обмеження
ALTER TABLE Persons
ADD CONSTRAINT PK_Persons PRIMARY KEY (ID);

-- Видалити обмеження
ALTER TABLE Persons
DROP CONSTRAINT PK_Persons;
```

Детальніше — у розділі [Обмеження](constraints.html).
