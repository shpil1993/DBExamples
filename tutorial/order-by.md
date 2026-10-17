---
title: "ORDER BY"
h1: "Ключове слово ORDER BY"
---

`ORDER BY` використовується для сортування результату за зростанням або спаданням.

* `ASC` — за зростанням (використовується за замовчуванням);
* `DESC` — за спаданням.

## Синтаксис

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

<div class="example" markdown="1">

Вибрати всі товари, відсортовані за ціною:

```sql
SELECT ProductName, Price
FROM Products
ORDER BY Price;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Tunnbröd</td><td>9.00</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td></tr>
<tr><td>Pavlova</td><td>17.45</td></tr>
<tr><td>Chais</td><td>18.00</td></tr>
<tr><td>Chang</td><td>19.00</td></tr>
</table></div>
<p class="result-more">… показано 5 з 15 рядків</p>
<!-- run:end -->

</div>

## DESC

<div class="example" markdown="1">

Відсортувати товари за ціною від найдорожчого:

```sql
SELECT ProductName, Price
FROM Products
ORDER BY Price DESC;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>Vegie-spread</td><td>43.90</td></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>40.00</td></tr>
<tr><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
<tr><td>Ikura</td><td>31.00</td></tr>
</table></div>
<p class="result-more">… показано 5 з 15 рядків</p>
<!-- run:end -->

</div>

## Сортування за алфавітом

Для текстових стовпців `ORDER BY` сортує за алфавітом:

<div class="example" markdown="1">

```sql
SELECT ProductName
FROM Products
ORDER BY ProductName;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th></tr>
<tr><td>Aniseed Syrup</td></tr>
<tr><td>Chais</td></tr>
<tr><td>Chang</td></tr>
<tr><td>Chef Anton's Cajun Seasoning</td></tr>
<tr><td>Chef Anton's Gumbo Mix</td></tr>
</table></div>
<p class="result-more">… показано 5 з 15 рядків</p>
<!-- run:end -->

</div>

## Сортування за кількома стовпцями

Спочатку рядки сортуються за першим стовпцем, а рядки з однаковим значенням — за другим.

<div class="example" markdown="1">

Відсортувати клієнтів за країною, а всередині країни — за назвою за спаданням:

```sql
SELECT CustomerName, Country
FROM Customers
ORDER BY Country ASC, CustomerName DESC;
```

<!-- run:start rows=13 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Country</th></tr>
<tr><td>Bottom-Dollar Marketse</td><td>Canada</td></tr>
<tr><td>Bon app'</td><td>France</td></tr>
<tr><td>Blondel père et fils</td><td>France</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Germany</td></tr>
<tr><td>Alfreds Futterkiste</td><td>Germany</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>Mexico</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>Mexico</td></tr>
<tr><td>Bólido Comidas preparadas</td><td>Spain</td></tr>
<tr><td>Berglunds snabbköp</td><td>Sweden</td></tr>
<tr><td>Around the Horn</td><td>UK</td></tr>
<tr><td>Odesa Seafood</td><td>Ukraine</td></tr>
<tr><td>Lviv Coffee House</td><td>Ukraine</td></tr>
<tr><td>Kyiv Market</td><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 13</p>
<!-- run:end -->

</div>

## Сортування за виразом або псевдонімом

У `ORDER BY` можна використовувати псевдоніми зі списку `SELECT` та вирази:

<div class="example" markdown="1">

```sql
SELECT ProductName, Price * 1.2 AS PriceWithVAT
FROM Products
ORDER BY PriceWithVAT DESC;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>PriceWithVAT</th></tr>
<tr><td>Mishi Kobe Niku</td><td>116.400</td></tr>
<tr><td>Vegie-spread</td><td>52.680</td></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>48.000</td></tr>
</table></div>
<p class="result-more">… показано 3 з 15 рядків</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
* Без `ORDER BY` SQL Server **не гарантує** жодного порядку рядків — навіть якщо зараз вони виводяться «по порядку».
* Значення `NULL` при сортуванні `ASC` йдуть першими, а при `DESC` — останніми.
</div>
