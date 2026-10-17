---
title: ANY та ALL
h1: Оператори ANY та ALL
---

Оператори `ANY` та `ALL` дають змогу порівняти одне значення з **набором** значень, які повертає підзапит.

## Оператор ANY

* повертає `TRUE`, якщо умова виконується **хоча б для одного** значення з підзапиту;
* `SOME` — синонім `ANY`.

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
    (SELECT column_name FROM table_name WHERE condition);
```

`operator` — оператор порівняння: `=`, `<>`, `!=`, `>`, `>=`, `<`, `<=`.

<div class="example" markdown="1">

Товари, які хоча б раз замовляли в кількості рівно 10 штук:

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY (
    SELECT ProductID FROM OrderDetails WHERE Quantity = 10
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th></tr>
<tr><td>Chais</td></tr>
<tr><td>Mishi Kobe Niku</td></tr>
<tr><td>Queso Manchego La Pastora</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Товари, які хоча б раз замовляли в кількості понад 40 штук:

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ANY (
    SELECT ProductID FROM OrderDetails WHERE Quantity > 40
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th></tr>
<tr><td>Northwoods Cranberry Sauce</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
`= ANY (...)` працює так само, як `IN (...)`.
</div>

## Оператор ALL

* повертає `TRUE`, якщо умова виконується **для всіх** значень з підзапиту;
* використовується в `WHERE` та `HAVING`.

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ALL
    (SELECT column_name FROM table_name WHERE condition);
```

<div class="example" markdown="1">

Товари, дорожчі за **всі** товари категорії 2 (Condiments):

```sql
SELECT ProductName, Price
FROM Products
WHERE Price > ALL (
    SELECT Price FROM Products WHERE CategoryID = 2
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Товари, дешевші за будь-який товар категорії 4 (Dairy Products):

```sql
SELECT ProductName, Price
FROM Products
WHERE Price < ALL (
    SELECT Price FROM Products WHERE CategoryID = 4
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Chais</td><td>18.00</td></tr>
<tr><td>Chang</td><td>19.00</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td></tr>
<tr><td>Pavlova</td><td>17.45</td></tr>
<tr><td>Tunnbröd</td><td>9.00</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
Якщо підзапит повертає **порожній** набір, умова з `ALL` вважається істинною для всіх рядків, а умова з `ANY` — хибною.
</div>
