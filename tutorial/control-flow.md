---
title: "IF...ELSE та WHILE"
h1: "Керування потоком: IF...ELSE, WHILE"
---

T-SQL має конструкції для керування порядком виконання: умови, блоки та цикли.

## BEGIN...END

`BEGIN ... END` об'єднує кілька інструкцій в один блок (як фігурні дужки в інших мовах):

```sql
BEGIN
    statement1;
    statement2;
END
```

## IF...ELSE

```sql
IF condition
    statement_or_block
[ELSE
    statement_or_block]
```

<div class="example" markdown="1">

```sql
DECLARE @Count INT = (SELECT COUNT(*) FROM Customers WHERE Country = N'Ukraine');

IF @Count > 0
BEGIN
    PRINT N'Клієнтів з України: ' + CAST(@Count AS NVARCHAR(10));
    SELECT CustomerName FROM Customers WHERE Country = N'Ukraine';
END
ELSE
    PRINT N'Клієнтів з України немає';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Kyiv Market</td></tr>
<tr><td>Lviv Coffee House</td></tr>
<tr><td>Odesa Seafood</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
Без `BEGIN ... END` до `IF` належить **лише одна** наступна інструкція. Решта виконуватиметься завжди.
</div>

### IF EXISTS

```sql
IF EXISTS (SELECT 1 FROM Products WHERE Price > 90)
    PRINT N'Є дуже дорогі товари';
```

### Вкладені IF та ELSE IF

<div class="example" markdown="1">

```sql
DECLARE @Price DECIMAL(10,2) = (SELECT Price FROM Products WHERE ProductID = 9);

IF @Price < 20
    SELECT N'Дешевий' AS Category;
ELSE IF @Price < 50
    SELECT N'Середній' AS Category;
ELSE
    SELECT N'Дорогий' AS Category;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Category</th></tr>
<tr><td>Дорогий</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## WHILE

Цикл `WHILE` повторює інструкцію або блок, поки умова істинна:

```sql
WHILE condition
BEGIN
    statements
END
```

<div class="example" markdown="1">

Таблиця множення на 3:

```sql
DECLARE @i INT = 1;
DECLARE @Result TABLE (Expression NVARCHAR(20), Value INT);

WHILE @i <= 5
BEGIN
    INSERT INTO @Result VALUES (CONCAT(N'3 x ', @i), 3 * @i);
    SET @i += 1;
END

SELECT * FROM @Result;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Expression</th><th>Value</th></tr>
<tr><td>3 x 1</td><td>3</td></tr>
<tr><td>3 x 2</td><td>6</td></tr>
<tr><td>3 x 3</td><td>9</td></tr>
<tr><td>3 x 4</td><td>12</td></tr>
<tr><td>3 x 5</td><td>15</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

## BREAK і CONTINUE

* `BREAK` — негайно виходить з циклу;
* `CONTINUE` — переходить до наступної ітерації.

<div class="example" markdown="1">

```sql
DECLARE @n INT = 0;
DECLARE @Odd NVARCHAR(100) = N'';

WHILE 1 = 1
BEGIN
    SET @n += 1;
    IF @n > 9 BREAK;          -- вихід з циклу
    IF @n % 2 = 0 CONTINUE;   -- пропустити парні
    SET @Odd += CAST(@n AS NVARCHAR(2)) + N' ';
END

SELECT @Odd AS OddNumbers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OddNumbers</th></tr>
<tr><td>1 3 5 7 9 </td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## WAITFOR

`WAITFOR` призупиняє виконання на заданий час або до певного моменту:

```sql
WAITFOR DELAY '00:00:05';   -- чекати 5 секунд
WAITFOR TIME '23:00';       -- чекати до 23:00
```

## RETURN

`RETURN` негайно завершує виконання пакета або процедури. У збереженій процедурі `RETURN` може повертати ціле число — код результату.

<div class="note" markdown="1">
SQL — мова, орієнтована на роботу з **множинами** рядків. Цикли `WHILE`, які обробляють рядки по одному, зазвичай значно повільніші за один запит `UPDATE` або `INSERT ... SELECT`. Використовуйте цикли лише тоді, коли задачу неможливо розв'язати одним запитом.
</div>
