---
title: "Робота з датами"
h1: "Робота з датами в SQL Server"
---

Найскладніше в роботі з датами — переконатися, що формат дати, яку ви вставляєте чи шукаєте, відповідає формату стовпця.

Поки дані містять лише дату, запити працюють передбачувано. Коли ж з'являється ще й час, усе ускладнюється.

## Типи даних для дат і часу

| Тип | Формат | Діапазон | Точність |
|---|---|---|---|
| `DATE` | `YYYY-MM-DD` | 0001-01-01 … 9999-12-31 | 1 день |
| `TIME` | `hh:mm:ss[.nnnnnnn]` | 00:00:00 … 23:59:59.9999999 | 100 нс |
| `DATETIME` | `YYYY-MM-DD hh:mm:ss[.nnn]` | 1753-01-01 … 9999-12-31 | ≈3,33 мс |
| `SMALLDATETIME` | `YYYY-MM-DD hh:mm:ss` | 1900-01-01 … 2079-06-06 | 1 хвилина |
| `DATETIME2` | `YYYY-MM-DD hh:mm:ss[.nnnnnnn]` | 0001-01-01 … 9999-12-31 | 100 нс |
| `DATETIMEOFFSET` | як `DATETIME2` + зсув часового поясу | 0001-01-01 … 9999-12-31 | 100 нс |

<div class="note" markdown="1">
Для нових таблиць Microsoft рекомендує `DATE`, `TIME`, `DATETIME2` і `DATETIMEOFFSET` замість застарілих `DATETIME` та `SMALLDATETIME`.
</div>

## Поточна дата й час

<div class="example" markdown="1">

```sql
SELECT GETDATE()          AS [GETDATE],          -- DATETIME
       SYSDATETIME()      AS [SYSDATETIME],      -- DATETIME2(7)
       CAST(GETDATE() AS DATE) AS Today,
       SYSDATETIMEOFFSET() AS WithTimeZone;
```

</div>

## Пошук за датою

<div class="example" markdown="1">

Замовлення від 8 липня 2024 року:

```sql
SELECT * FROM Orders WHERE OrderDate = '2024-07-08';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerID</th><th>EmployeeID</th><th>OrderDate</th><th>ShipperID</th></tr>
<tr><td>10250</td><td>3</td><td>4</td><td>2024-07-08</td><td>2</td></tr>
<tr><td>10251</td><td>7</td><td>3</td><td>2024-07-08</td><td>1</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Записуйте дати у форматі ISO `'YYYY-MM-DD'` для `DATE` або `'YYYYMMDD'` — ці формати SQL Server розуміє однаково за будь-яких мовних налаштувань. Формат на кшталт `'08/07/2024'` може бути прочитаний і як 8 липня, і як 7 серпня!
</div>

## Дата з часом

Припустимо, стовпець `OrderDate` мав би тип `DATETIME2` і містив значення `2024-07-08 14:55:10`. Тоді запит

```sql
SELECT * FROM Orders WHERE OrderDate = '2024-07-08';
```

не поверне цей рядок, бо `'2024-07-08'` означає `2024-07-08 00:00:00`. Правильні способи:

```sql
-- 1. Півінтервал (найкращий варіант: може використовувати індекс)
SELECT * FROM Orders
WHERE OrderDate >= '2024-07-08' AND OrderDate < '2024-07-09';

-- 2. Перетворення на DATE
SELECT * FROM Orders
WHERE CAST(OrderDate AS DATE) = '2024-07-08';
```

<div class="warn" markdown="1">
Щоб запити з датами були простими, не зберігайте час, якщо він не потрібен — використовуйте тип `DATE`.
</div>

## Частини дати

<div class="example" markdown="1">

```sql
SELECT OrderID, OrderDate,
       YEAR(OrderDate)  AS [Year],
       MONTH(OrderDate) AS [Month],
       DAY(OrderDate)   AS [Day],
       DATENAME(WEEKDAY, OrderDate) AS WeekDay
FROM Orders
WHERE OrderID < 10251;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>OrderDate</th><th>Year</th><th>Month</th><th>Day</th><th>WeekDay</th></tr>
<tr><td>10248</td><td>2024-07-04</td><td>2024</td><td>7</td><td>4</td><td>Thursday</td></tr>
<tr><td>10249</td><td>2024-07-05</td><td>2024</td><td>7</td><td>5</td><td>Friday</td></tr>
<tr><td>10250</td><td>2024-07-08</td><td>2024</td><td>7</td><td>8</td><td>Monday</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## Арифметика дат

<div class="example" markdown="1">

Скільки днів минуло від першого до останнього замовлення, і яка дата буде через 30 днів після першого:

```sql
SELECT DATEDIFF(DAY, MIN(OrderDate), MAX(OrderDate)) AS DaysBetween,
       DATEADD(DAY, 30, MIN(OrderDate))              AS FirstPlus30
FROM Orders;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>DaysBetween</th><th>FirstPlus30</th></tr>
<tr><td>151</td><td>2024-08-03</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Вік працівників на 1 січня 2025 року (приблизно, у роках):

```sql
SELECT FirstName, LastName, BirthDate,
       DATEDIFF(YEAR, BirthDate, '2025-01-01') AS Age
FROM Employees;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>FirstName</th><th>LastName</th><th>BirthDate</th><th>Age</th></tr>
<tr><td>Andrew</td><td>Fuller</td><td>1952-02-19</td><td>73</td></tr>
<tr><td>Nancy</td><td>Davolio</td><td>1968-12-08</td><td>57</td></tr>
<tr><td>Janet</td><td>Leverling</td><td>1963-08-30</td><td>62</td></tr>
</table></div>
<p class="result-more">… показано 3 з 7 рядків</p>
<!-- run:end -->

</div>

## Форматування дат

<div class="example" markdown="1">

```sql
SELECT FORMAT(CAST('2024-07-08' AS DATE), 'dd.MM.yyyy')          AS UA,
       FORMAT(CAST('2024-07-08' AS DATE), 'D', 'uk-UA')          AS UALong,
       CONVERT(VARCHAR(10), CAST('2024-07-08' AS DATE), 104)     AS Style104;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>UA</th><th>UALong</th><th>Style104</th></tr>
<tr><td>08.07.2024</td><td>8 липня 2024 р.</td><td>08.07.2024</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Повний перелік функцій — у довіднику [Функції дати й часу](date-functions.html).
