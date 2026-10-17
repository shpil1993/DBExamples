---
title: "INNER JOIN"
h1: "INNER JOIN"
---

`INNER JOIN` вибирає рядки, для яких є відповідні значення в **обох** таблицях.

## Синтаксис

```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
    ON table1.column_name = table2.column_name;
```

<div class="note" markdown="1">
Ключове слово `INNER` можна пропустити: просто `JOIN` означає те саме, що й `INNER JOIN`.
</div>

## Приклад

<div class="example" markdown="1">

Вибрати замовлення з іменами клієнтів:

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerName</th></tr>
<tr><td>10248</td><td>Around the Horn</td></tr>
<tr><td>10249</td><td>Alfreds Futterkiste</td></tr>
<tr><td>10250</td><td>Antonio Moreno Taquería</td></tr>
<tr><td>10251</td><td>Blondel père et fils</td></tr>
<tr><td>10252</td><td>Ana Trujillo Emparedados y helados</td></tr>
</table></div>
<p class="result-more">… показано 5 з 14 рядків</p>
<!-- run:end -->

</div>

`INNER JOIN` повертає лише ті рядки, для яких знайшовся збіг. Клієнти без замовлень (наприклад, *Blauer See Delikatessen*) у результат не потрапляють.

## Імена стовпців і псевдоніми

Якщо стовпець з однаковою назвою є в обох таблицях (як `CustomerID`), його потрібно вказувати з ім'ям або псевдонімом таблиці. Зазвичай використовують короткі псевдоніми:

<div class="example" markdown="1">

Товари з назвами їхніх категорій:

```sql
SELECT p.ProductID, p.ProductName, c.CategoryName
FROM Products AS p
INNER JOIN Categories AS c ON p.CategoryID = c.CategoryID;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductID</th><th>ProductName</th><th>CategoryName</th></tr>
<tr><td>1</td><td>Chais</td><td>Beverages</td></tr>
<tr><td>2</td><td>Chang</td><td>Beverages</td></tr>
<tr><td>3</td><td>Aniseed Syrup</td><td>Condiments</td></tr>
<tr><td>4</td><td>Chef Anton's Cajun Seasoning</td><td>Condiments</td></tr>
<tr><td>5</td><td>Chef Anton's Gumbo Mix</td><td>Condiments</td></tr>
</table></div>
<p class="result-more">… показано 5 з 15 рядків</p>
<!-- run:end -->

</div>

## З'єднання трьох таблиць

<div class="example" markdown="1">

Замовлення з іменами клієнтів та служб доставки:

```sql
SELECT o.OrderID, c.CustomerName, s.ShipperName
FROM Orders AS o
INNER JOIN Customers AS c ON o.CustomerID = c.CustomerID
INNER JOIN Shippers  AS s ON o.ShipperID  = s.ShipperID;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerName</th><th>ShipperName</th></tr>
<tr><td>10248</td><td>Around the Horn</td><td>Federal Shipping</td></tr>
<tr><td>10249</td><td>Alfreds Futterkiste</td><td>Speedy Express</td></tr>
<tr><td>10250</td><td>Antonio Moreno Taquería</td><td>United Package</td></tr>
<tr><td>10251</td><td>Blondel père et fils</td><td>Speedy Express</td></tr>
<tr><td>10252</td><td>Ana Trujillo Emparedados y helados</td><td>United Package</td></tr>
</table></div>
<p class="result-more">… показано 5 з 14 рядків</p>
<!-- run:end -->

</div>

## Більш складний приклад

<div class="example" markdown="1">

Склад замовлення 10248: назва товару, кількість, ціна та сума:

```sql
SELECT od.OrderID, p.ProductName, od.Quantity, p.Price,
       od.Quantity * p.Price AS LineTotal
FROM OrderDetails AS od
JOIN Products AS p ON od.ProductID = p.ProductID
WHERE od.OrderID = 10248;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>ProductName</th><th>Quantity</th><th>Price</th><th>LineTotal</th></tr>
<tr><td>10248</td><td>Queso Cabrales</td><td>12</td><td>21.00</td><td>252.00</td></tr>
<tr><td>10248</td><td>Mishi Kobe Niku</td><td>10</td><td>97.00</td><td>970.00</td></tr>
<tr><td>10248</td><td>Vegie-spread</td><td>5</td><td>43.90</td><td>219.50</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>
