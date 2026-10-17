---
title: "SELECT INTO"
h1: "Інструкція SELECT INTO"
---

Інструкція `SELECT INTO` копіює дані з однієї таблиці в **нову** таблицю.

Нова таблиця створюється автоматично зі стовпцями й типами даних, як у результаті запиту.

<div class="note" markdown="1">
У MySQL такої інструкції немає (там використовують `CREATE TABLE ... AS SELECT`). У SQL Server, навпаки, немає `CREATE TABLE ... AS SELECT` — використовується `SELECT INTO`.
</div>

## Синтаксис

Скопіювати всі стовпці:

```sql
SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
```

Скопіювати лише деякі стовпці:

```sql
SELECT column1, column2, column3, ...
INTO newtable
FROM oldtable
WHERE condition;
```

## Приклади

<div class="example" markdown="1">

Створити резервну копію таблиці `Customers`:

```sql
SELECT * INTO CustomersBackup2024
FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 13</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Скопіювати в нову таблицю лише клієнтів з Німеччини:

```sql
SELECT * INTO CustomersGermany
FROM Customers
WHERE Country = N'Germany';
```

</div>

<div class="example" markdown="1">

Скопіювати дані з кількох таблиць:

```sql
SELECT c.CustomerName, o.OrderID, o.OrderDate
INTO CustomersOrderBackup2024
FROM Customers AS c
LEFT JOIN Orders AS o ON c.CustomerID = o.CustomerID;
```

</div>

<div class="example" markdown="1">

Скопіювати в іншу базу даних (вказавши повне ім'я `база.схема.таблиця`):

```sql
SELECT * INTO ArchiveDb.dbo.CustomersBackup
FROM Customers;
```

</div>

## Порожня копія структури

Щоб створити порожню таблицю з такою самою структурою, додайте умову, яка ніколи не виконується:

```sql
SELECT * INTO NewCustomers
FROM Customers
WHERE 1 = 0;
```

## Тимчасові таблиці

`SELECT INTO` часто використовують для створення **тимчасових таблиць** — їхня назва починається з `#`. Тимчасова таблиця існує лише в поточному сеансі й автоматично видаляється після його завершення:

<div class="example" markdown="1">

```sql
SELECT ProductName, Price
INTO #Expensive
FROM Products
WHERE Price > 30;

SELECT * FROM #Expensive;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>40.00</td></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>Ikura</td><td>31.00</td></tr>
<tr><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
<tr><td>Vegie-spread</td><td>43.90</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
`SELECT INTO` не копіює первинні ключі, індекси, обмеження та тригери — лише стовпці, типи даних і властивість `IDENTITY`.
</div>
