---
title: "IDENTITY (автоінкремент)"
h1: "IDENTITY — автоматичне нумерування"
---

Властивість `IDENTITY` автоматично генерує унікальне число при вставленні нового рядка в таблицю.

Найчастіше її використовують для стовпця первинного ключа, щоб сервер сам присвоював номери записам. У MySQL аналогічна можливість називається `AUTO_INCREMENT`.

## Синтаксис

```sql
column_name INT IDENTITY(seed, increment)
```

* `seed` — початкове значення (для першого рядка);
* `increment` — крок, на який збільшується значення для кожного наступного рядка.

Якщо параметри не вказати, використовується `IDENTITY(1,1)`.

## Приклад

<div class="example" markdown="1">

```sql
CREATE TABLE Persons (
    PersonID  INT IDENTITY(1,1) PRIMARY KEY,
    LastName  NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(255),
    Age       INT
);

INSERT INTO Persons (FirstName, LastName) VALUES (N'Lars', N'Monsen');
INSERT INTO Persons (FirstName, LastName) VALUES (N'Olena', N'Pchilka');

SELECT * FROM Persons;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>PersonID</th><th>LastName</th><th>FirstName</th><th>Age</th></tr>
<tr><td>1</td><td>Monsen</td><td>Lars</td><td><span class="null">NULL</span></td></tr>
<tr><td>2</td><td>Pchilka</td><td>Olena</td><td><span class="null">NULL</span></td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

Значення для `PersonID` при вставленні не вказується — його генерує SQL Server.

## Інше початкове значення і крок

<div class="example" markdown="1">

Нумерація з 100 з кроком 10:

```sql
CREATE TABLE Tickets (
    TicketID INT IDENTITY(100, 10) PRIMARY KEY,
    Title    NVARCHAR(100)
);

INSERT INTO Tickets (Title) VALUES (N'Перший'), (N'Другий'), (N'Третій');
SELECT * FROM Tickets;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>TicketID</th><th>Title</th></tr>
<tr><td>100</td><td>Перший</td></tr>
<tr><td>110</td><td>Другий</td></tr>
<tr><td>120</td><td>Третій</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## Отримання останнього значення

| Функція | Що повертає |
|---|---|
| `SCOPE_IDENTITY()` | Останнє значення `IDENTITY` у поточному сеансі **та області видимості** (рекомендується) |
| `@@IDENTITY` | Останнє значення в сеансі, включно з тими, що згенерували тригери |
| `IDENT_CURRENT('table')` | Останнє значення для таблиці в **будь-якому** сеансі |

<div class="example" markdown="1">

```sql
INSERT INTO Shippers (ShipperName) VALUES (N'Nova Poshta');
SELECT SCOPE_IDENTITY() AS NewShipperID;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>NewShipperID</th></tr>
<tr><td>4</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Явне вставлення значення

За замовчуванням вставити власне значення в стовпець `IDENTITY` не можна. Якщо це дійсно потрібно (наприклад, при перенесенні даних), увімкніть `IDENTITY_INSERT`:

```sql
SET IDENTITY_INSERT Shippers ON;

INSERT INTO Shippers (ShipperID, ShipperName) VALUES (100, N'Special Delivery');

SET IDENTITY_INSERT Shippers OFF;
```

## Скидання лічильника

```sql
-- Наступне значення буде 1 (якщо таблиця порожня)
DBCC CHECKIDENT ('Persons', RESEED, 0);
```

`TRUNCATE TABLE` також скидає лічильник `IDENTITY` до початкового значення.

<div class="warn" markdown="1">
`IDENTITY` **не гарантує** відсутності «дірок» у нумерації. Якщо транзакцію відкотити або сервер перезапуститься, деякі номери можуть бути пропущені. Не використовуйте `IDENTITY`, якщо потрібна безперервна нумерація (наприклад, номери рахунків-фактур).
</div>

## SEQUENCE

Альтернатива `IDENTITY` — об'єкт `SEQUENCE`. Він не прив'язаний до таблиці й може використовуватися кількома таблицями:

<div class="example" markdown="1">

```sql
CREATE SEQUENCE dbo.InvoiceNumbers
    START WITH 1000
    INCREMENT BY 1;
GO
SELECT NEXT VALUE FOR dbo.InvoiceNumbers AS First,
       NEXT VALUE FOR dbo.InvoiceNumbers AS Same;
SELECT NEXT VALUE FOR dbo.InvoiceNumbers AS Next;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>First</th><th>Same</th></tr>
<tr><td>1000</td><td>1000</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<div class="table-scroll"><table>
<tr><th>Next</th></tr>
<tr><td>1001</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Зверніть увагу: в одній інструкції `SELECT` кілька викликів `NEXT VALUE FOR` для однієї послідовності повертають **однакове** значення.
</div>
