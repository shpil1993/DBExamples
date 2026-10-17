---
title: "CROSS JOIN"
h1: "CROSS JOIN"
---

`CROSS JOIN` повертає **всі можливі комбінації** рядків з обох таблиць (декартовий добуток).

Якщо в першій таблиці 10 рядків, а в другій — 3, результат міститиме 10 × 3 = 30 рядків.

## Синтаксис

```sql
SELECT column_name(s)
FROM table1
CROSS JOIN table2;
```

<div class="note" markdown="1">
`CROSS JOIN` не має умови `ON`. На великих таблицях результат може бути величезним.
</div>

## Приклад

<div class="example" markdown="1">

Усі комбінації служб доставки та категорій товарів:

```sql
SELECT s.ShipperName, c.CategoryName
FROM Shippers AS s
CROSS JOIN Categories AS c
ORDER BY s.ShipperName, c.CategoryName;
```

<!-- run:start rows=8 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ShipperName</th><th>CategoryName</th></tr>
<tr><td>Federal Shipping</td><td>Beverages</td></tr>
<tr><td>Federal Shipping</td><td>Condiments</td></tr>
<tr><td>Federal Shipping</td><td>Confections</td></tr>
<tr><td>Federal Shipping</td><td>Dairy Products</td></tr>
<tr><td>Federal Shipping</td><td>Grains/Cereals</td></tr>
<tr><td>Federal Shipping</td><td>Meat/Poultry</td></tr>
<tr><td>Federal Shipping</td><td>Produce</td></tr>
<tr><td>Federal Shipping</td><td>Seafood</td></tr>
</table></div>
<p class="result-more">… показано 8 з 24 рядків</p>
<!-- run:end -->

</div>

## Коли використовувати CROSS JOIN?

* щоб згенерувати всі комбінації (наприклад, розмір × колір товару);
* щоб побудувати «сітку» для звіту (кожен місяць × кожен працівник), до якої потім приєднати фактичні дані через `LEFT JOIN`.

<div class="example" markdown="1">

Таблиця розмірів і кольорів, згенерована «на льоту» конструкцією `VALUES`:

```sql
SELECT s.Size, c.Color
FROM (VALUES (N'S'), (N'M'), (N'L')) AS s(Size)
CROSS JOIN (VALUES (N'Red'), (N'Blue')) AS c(Color);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Size</th><th>Color</th></tr>
<tr><td>S</td><td>Red</td></tr>
<tr><td>M</td><td>Red</td></tr>
<tr><td>L</td><td>Red</td></tr>
<tr><td>S</td><td>Blue</td></tr>
<tr><td>M</td><td>Blue</td></tr>
<tr><td>L</td><td>Blue</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

## CROSS APPLY

У SQL Server є споріднений оператор `CROSS APPLY`: він виконує праву частину (підзапит або табличну функцію) для **кожного рядка** лівої таблиці. Наприклад, два найдорожчі товари в кожній категорії:

<div class="example" markdown="1">

```sql
SELECT c.CategoryName, t.ProductName, t.Price
FROM Categories AS c
CROSS APPLY (
    SELECT TOP (2) p.ProductName, p.Price
    FROM Products AS p
    WHERE p.CategoryID = c.CategoryID
    ORDER BY p.Price DESC
) AS t;
```

<!-- run:start rows=6 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CategoryName</th><th>ProductName</th><th>Price</th></tr>
<tr><td>Beverages</td><td>Chang</td><td>19.00</td></tr>
<tr><td>Beverages</td><td>Chais</td><td>18.00</td></tr>
<tr><td>Condiments</td><td>Vegie-spread</td><td>43.90</td></tr>
<tr><td>Condiments</td><td>Northwoods Cranberry Sauce</td><td>40.00</td></tr>
<tr><td>Confections</td><td>Pavlova</td><td>17.45</td></tr>
<tr><td>Dairy Products</td><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
</table></div>
<p class="result-more">… показано 6 з 11 рядків</p>
<!-- run:end -->

</div>

`OUTER APPLY` працює так само, але залишає рядки лівої таблиці, для яких права частина нічого не повернула (як `LEFT JOIN`).
