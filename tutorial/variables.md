---
title: "Змінні та пакети"
h1: "Змінні та пакети в T-SQL"
---

T-SQL — це не лише мова запитів, а й мова програмування. У ній є змінні, умови, цикли та обробка помилок.

## Оголошення змінної: DECLARE

Імена змінних починаються з символу `@`:

```sql
DECLARE @variable_name datatype [= initial_value];
```

<div class="example" markdown="1">

```sql
DECLARE @Country NVARCHAR(50) = N'Germany';
DECLARE @MinPrice DECIMAL(10,2), @Counter INT;

SELECT @Country AS Country, @MinPrice AS MinPrice, @Counter AS Counter;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th><th>MinPrice</th><th>Counter</th></tr>
<tr><td>Germany</td><td><span class="null">NULL</span></td><td><span class="null">NULL</span></td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Змінна без початкового значення містить `NULL`.

## Присвоєння значення: SET і SELECT

<div class="example" markdown="1">

```sql
DECLARE @Total INT;
DECLARE @MaxPrice DECIMAL(10,2);

SET @Total = (SELECT COUNT(*) FROM Customers);   -- SET: одне значення
SELECT @MaxPrice = MAX(Price) FROM Products;     -- SELECT: можна кілька

SELECT @Total AS Customers, @MaxPrice AS MaxPrice;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Customers</th><th>MaxPrice</th></tr>
<tr><td>13</td><td>97.00</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
`SET` присвоює одну змінну за раз. `SELECT @a = ..., @b = ...` може присвоїти кілька змінних одним запитом. Якщо запит повертає кілька рядків, `SELECT` присвоїть значення з **останнього** рядка, а `SET` з підзапитом поверне помилку.
</div>

## Використання змінних у запитах

<div class="example" markdown="1">

```sql
DECLARE @Country NVARCHAR(50) = N'Mexico';

SELECT CustomerName, City
FROM Customers
WHERE Country = @Country;
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

## Виведення повідомлень: PRINT

```sql
DECLARE @Name NVARCHAR(50) = N'SQL Server';
PRINT N'Привіт, ' + @Name + N'!';
```

`PRINT` виводить текст на вкладку **Messages** у SSMS. Це зручно для налагодження.

## Табличні змінні

Змінна може мати тип `TABLE` — це невелика тимчасова таблиця, що існує до кінця пакета:

<div class="example" markdown="1">

```sql
DECLARE @TopProducts TABLE (
    ProductName NVARCHAR(100),
    Price       DECIMAL(10,2)
);

INSERT INTO @TopProducts (ProductName, Price)
SELECT TOP (3) ProductName, Price FROM Products ORDER BY Price DESC;

SELECT * FROM @TopProducts;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>Vegie-spread</td><td>43.90</td></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>40.00</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## Системні функції з @@

Деякі вбудовані функції мають імена з префіксом `@@`:

| Функція | Що повертає |
|---|---|
| `@@ROWCOUNT` | Кількість рядків, оброблених останньою інструкцією |
| `@@ERROR` | Номер помилки останньої інструкції (0 — без помилок) |
| `@@VERSION` | Версію SQL Server |
| `@@SERVERNAME` | Ім'я сервера |
| `@@SPID` | Ідентифікатор поточного сеансу |
| `@@TRANCOUNT` | Кількість відкритих транзакцій |

<div class="example" markdown="1">

```sql
UPDATE Products SET Price = Price WHERE CategoryID = 2;
SELECT @@ROWCOUNT AS UpdatedRows;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>UpdatedRows</th></tr>
<tr><td>6</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Пакети та GO

**Пакет** (batch) — група інструкцій, яку клієнт надсилає на сервер одночасно. SQL Server компілює пакет цілком, а потім виконує.

У SSMS, VS Code і sqlcmd пакети розділяються рядком `GO`. `GO` — не інструкція T-SQL, а команда для клієнтської програми.

```sql
DECLARE @x INT = 5;
PRINT @x;      -- 5
GO
PRINT @x;      -- Помилка: змінна @x не оголошена
```

Важливо:

* **змінні існують лише в межах пакета**, де вони оголошені;
* інструкції `CREATE VIEW`, `CREATE PROCEDURE`, `CREATE FUNCTION`, `CREATE TRIGGER` мають бути першими в пакеті;
* `GO 5` виконає попередній пакет 5 разів.
