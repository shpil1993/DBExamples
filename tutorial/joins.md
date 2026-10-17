---
title: З'єднання (Joins)
h1: З'єднання таблиць (JOIN)
---

`JOIN` використовується, щоб об'єднати рядки двох або більше таблиць на основі пов'язаного стовпця.

Подивимося на фрагмент таблиці `Orders`:

```sql
SELECT TOP (3) OrderID, CustomerID, OrderDate FROM Orders;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerID</th><th>OrderDate</th></tr>
<tr><td>10248</td><td>4</td><td>2024-07-04</td></tr>
<tr><td>10249</td><td>1</td><td>2024-07-05</td></tr>
<tr><td>10250</td><td>3</td><td>2024-07-08</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

і на фрагмент таблиці `Customers`:

```sql
SELECT CustomerID, CustomerName, Country FROM Customers
WHERE CustomerID IN (1, 3, 4);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>Country</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td><td>Germany</td></tr>
<tr><td>3</td><td>Antonio Moreno Taquería</td><td>Mexico</td></tr>
<tr><td>4</td><td>Around the Horn</td><td>UK</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

Стовпець `CustomerID` у таблиці `Orders` посилається на `CustomerID` у таблиці `Customers`. Це і є зв'язок між таблицями.

Створимо запит з `INNER JOIN`, який вибирає записи з однаковими значеннями в обох таблицях:

<div class="example" markdown="1">

```sql
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerName</th><th>OrderDate</th></tr>
<tr><td>10248</td><td>Around the Horn</td><td>2024-07-04</td></tr>
<tr><td>10249</td><td>Alfreds Futterkiste</td><td>2024-07-05</td></tr>
<tr><td>10250</td><td>Antonio Moreno Taquería</td><td>2024-07-08</td></tr>
<tr><td>10251</td><td>Blondel père et fils</td><td>2024-07-08</td></tr>
<tr><td>10252</td><td>Ana Trujillo Emparedados y helados</td><td>2024-07-09</td></tr>
</table></div>
<p class="result-more">… показано 5 з 14 рядків</p>
<!-- run:end -->

</div>

## Типи JOIN у SQL Server

| Тип | Що повертає |
|---|---|
| [`INNER JOIN`](inner-join.html) | Рядки, для яких є збіг в **обох** таблицях |
| [`LEFT JOIN`](left-join.html) | **Усі** рядки з лівої таблиці та збіги з правої |
| [`RIGHT JOIN`](right-join.html) | **Усі** рядки з правої таблиці та збіги з лівої |
| [`FULL JOIN`](full-join.html) | Усі рядки з обох таблиць, з'єднуючи ті, що збігаються |
| [`CROSS JOIN`](cross-join.html) | Усі можливі комбінації рядків (декартовий добуток) |

<svg viewBox="0 0 640 130" role="img" aria-label="Діаграми INNER, LEFT, RIGHT і FULL JOIN" style="max-width:640px;width:100%;margin:12px 0">
  <style>
    .jl{fill:none;stroke:currentColor;stroke-width:1.5}
    .jf{fill:var(--accent);opacity:.55}
    .jt{fill:currentColor;font:13px sans-serif;text-anchor:middle}
  </style>
  <defs>
    <clipPath id="cA1"><circle cx="55" cy="55" r="38"/></clipPath>
  </defs>
  <!-- INNER -->
  <g>
    <circle class="jf" cx="80" cy="55" r="38" clip-path="url(#cA1)"/>
    <circle class="jl" cx="55" cy="55" r="38"/><circle class="jl" cx="80" cy="55" r="38"/>
    <text class="jt" x="68" y="120">INNER JOIN</text>
  </g>
  <!-- LEFT -->
  <g transform="translate(160,0)">
    <circle class="jf" cx="55" cy="55" r="38"/>
    <circle class="jl" cx="55" cy="55" r="38"/><circle class="jl" cx="80" cy="55" r="38"/>
    <text class="jt" x="68" y="120">LEFT JOIN</text>
  </g>
  <!-- RIGHT -->
  <g transform="translate(320,0)">
    <circle class="jf" cx="80" cy="55" r="38"/>
    <circle class="jl" cx="55" cy="55" r="38"/><circle class="jl" cx="80" cy="55" r="38"/>
    <text class="jt" x="68" y="120">RIGHT JOIN</text>
  </g>
  <!-- FULL -->
  <g transform="translate(480,0)">
    <circle class="jf" cx="55" cy="55" r="38"/><circle class="jf" cx="80" cy="55" r="38"/>
    <circle class="jl" cx="55" cy="55" r="38"/><circle class="jl" cx="80" cy="55" r="38"/>
    <text class="jt" x="68" y="120">FULL JOIN</text>
  </g>
</svg>

Ліве коло — ліва таблиця (та, що в `FROM`), праве — права таблиця (та, що після `JOIN`). Заштрихована область — рядки, які потрапляють у результат.

<div class="note" markdown="1">
**MySQL і SQL Server.** У MySQL немає `FULL JOIN`, тому на сайтах про MySQL його емулюють через `UNION`. У SQL Server `FULL OUTER JOIN` підтримується напряму.
</div>

## Старий синтаксис з'єднання

З'єднати таблиці можна й через перелік у `FROM` з умовою у `WHERE`:

```sql
SELECT o.OrderID, c.CustomerName
FROM Orders o, Customers c
WHERE o.CustomerID = c.CustomerID;
```

Це працює так само, як `INNER JOIN`, але явний синтаксис `JOIN ... ON` читається краще і рекомендований до використання.
