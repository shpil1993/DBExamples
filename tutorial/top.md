---
title: TOP та OFFSET FETCH
h1: TOP та OFFSET ... FETCH
---

У MySQL для обмеження кількості рядків використовується `LIMIT`. У SQL Server для цього є два інструменти:

* `TOP` — повертає перші N рядків;
* `OFFSET ... FETCH` — пропускає певну кількість рядків і повертає наступні N (зручно для посторінкового виводу).

## Синтаксис TOP

```sql
SELECT TOP (number) [PERCENT] [WITH TIES] column_name(s)
FROM table_name
WHERE condition
ORDER BY column_name(s);
```

<div class="example" markdown="1">

Вибрати перших трьох клієнтів:

```sql
SELECT TOP (3) * FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>ContactName</th><th>Address</th><th>City</th><th>PostalCode</th><th>Country</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Obere Str. 57</td><td>Berlin</td><td>12209</td><td>Germany</td></tr>
<tr><td>2</td><td>Ana Trujillo Emparedados y helados</td><td>Ana Trujillo</td><td>Avda. de la Constitución 2222</td><td>México D.F.</td><td>05021</td><td>Mexico</td></tr>
<tr><td>3</td><td>Antonio Moreno Taquería</td><td>Antonio Moreno</td><td>Mataderos 2312</td><td>México D.F.</td><td>05023</td><td>Mexico</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Без `ORDER BY` невідомо, які саме рядки будуть «першими». Для передбачуваного результату завжди використовуйте `TOP` разом з `ORDER BY`. Дужки в `TOP (3)` в `SELECT` необов'язкові, але рекомендовані.
</div>

## TOP з ORDER BY

<div class="example" markdown="1">

Три найдорожчі товари:

```sql
SELECT TOP (3) ProductName, Price
FROM Products
ORDER BY Price DESC;
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

## TOP ... PERCENT

<div class="example" markdown="1">

Вибрати перші 20% товарів за ціною:

```sql
SELECT TOP (20) PERCENT ProductName, Price
FROM Products
ORDER BY Price;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Tunnbröd</td><td>9.00</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td></tr>
<tr><td>Pavlova</td><td>17.45</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## TOP ... WITH TIES

`WITH TIES` додає до результату рядки, які мають таке саме значення в стовпцях `ORDER BY`, як і останній рядок:

<div class="example" markdown="1">

```sql
SELECT TOP (1) WITH TIES OrderID, OrderDate
FROM Orders
ORDER BY OrderDate;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>OrderDate</th></tr>
<tr><td>10248</td><td>2024-07-04</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## TOP з умовою WHERE

<div class="example" markdown="1">

```sql
SELECT TOP (2) CustomerName, Country
FROM Customers
WHERE Country = N'Ukraine'
ORDER BY CustomerName;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Country</th></tr>
<tr><td>Kyiv Market</td><td>Ukraine</td></tr>
<tr><td>Lviv Coffee House</td><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## OFFSET ... FETCH

`OFFSET ... FETCH` — частина речення `ORDER BY` (тому `ORDER BY` тут обов'язковий):

```sql
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s)
OFFSET skip_rows ROWS
FETCH NEXT take_rows ROWS ONLY;
```

<div class="example" markdown="1">

Пропустити 5 перших товарів і показати наступні 5 (друга «сторінка» по 5 товарів):

```sql
SELECT ProductID, ProductName
FROM Products
ORDER BY ProductID
OFFSET 5 ROWS
FETCH NEXT 5 ROWS ONLY;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductID</th><th>ProductName</th></tr>
<tr><td>6</td><td>Grandma's Boysenberry Spread</td></tr>
<tr><td>7</td><td>Uncle Bob's Organic Dried Pears</td></tr>
<tr><td>8</td><td>Northwoods Cranberry Sauce</td></tr>
<tr><td>9</td><td>Mishi Kobe Niku</td></tr>
<tr><td>10</td><td>Ikura</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Пропустити перші 10 рядків і показати всі решту (без `FETCH`):

```sql
SELECT ProductID, ProductName
FROM Products
ORDER BY ProductID
OFFSET 10 ROWS;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductID</th><th>ProductName</th></tr>
<tr><td>11</td><td>Queso Cabrales</td></tr>
<tr><td>12</td><td>Queso Manchego La Pastora</td></tr>
<tr><td>13</td><td>Pavlova</td></tr>
<tr><td>14</td><td>Vegie-spread</td></tr>
<tr><td>15</td><td>Tunnbröd</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

## Відповідність MySQL і SQL Server

| MySQL | SQL Server |
|---|---|
| `SELECT * FROM t LIMIT 3;` | `SELECT TOP (3) * FROM t;` |
| `SELECT * FROM t ORDER BY id LIMIT 5 OFFSET 10;` | `SELECT * FROM t ORDER BY id OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;` |

`TOP` також можна використовувати в `UPDATE` і `DELETE`, наприклад `DELETE TOP (100) FROM LogTable;`.
