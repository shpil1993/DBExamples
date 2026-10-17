---
title: "FULL JOIN"
h1: "FULL OUTER JOIN"
---

`FULL OUTER JOIN` (або просто `FULL JOIN`) повертає **всі** рядки з обох таблиць. Рядки, що мають збіг, об'єднуються; для рядків без збігу стовпці іншої таблиці отримують значення `NULL`.

## Синтаксис

```sql
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
    ON table1.column_name = table2.column_name
WHERE condition;
```

<div class="note" markdown="1">
`FULL JOIN` може повертати дуже великі результати, якщо таблиці великі.
</div>

## Приклад

<div class="example" markdown="1">

Вибрати всіх клієнтів і всі замовлення:

```sql
SELECT c.CustomerName, o.OrderID
FROM Customers AS c
FULL OUTER JOIN Orders AS o ON c.CustomerID = o.CustomerID
ORDER BY c.CustomerName;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>OrderID</th></tr>
<tr><td>Alfreds Futterkiste</td><td>10249</td></tr>
<tr><td>Alfreds Futterkiste</td><td>10260</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>10252</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>10250</td></tr>
<tr><td>Around the Horn</td><td>10248</td></tr>
<tr><td>Around the Horn</td><td>10253</td></tr>
<tr><td>Berglunds snabbköp</td><td>10254</td></tr>
<tr><td>Blauer See Delikatessen</td><td><span class="null">NULL</span></td></tr>
<tr><td>Blondel père et fils</td><td>10251</td></tr>
<tr><td>Bólido Comidas preparadas</td><td>10255</td></tr>
<tr><td>Bon app'</td><td>10256</td></tr>
<tr><td>Bottom-Dollar Marketse</td><td>10261</td></tr>
<tr><td>Kyiv Market</td><td>10257</td></tr>
<tr><td>Kyiv Market</td><td>10258</td></tr>
<tr><td>Lviv Coffee House</td><td>10259</td></tr>
<tr><td>Odesa Seafood</td><td><span class="null">NULL</span></td></tr>
</table></div>
<p class="result-more">Рядків: 16</p>
<!-- run:end -->

</div>

У результаті є і клієнти без замовлень, і (якби такі були) замовлення без клієнта.

## Приклад: пошук розбіжностей

`FULL JOIN` зручно використовувати для порівняння двох наборів даних. Знайдемо товари без постачальника та постачальників без товарів:

<div class="example" markdown="1">

```sql
SELECT s.SupplierName, p.ProductName
FROM Suppliers AS s
FULL JOIN Products AS p ON s.SupplierID = p.SupplierID
WHERE s.SupplierID IS NULL OR p.ProductID IS NULL;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>SupplierName</th><th>ProductName</th></tr>
<tr><td><span class="null">NULL</span></td><td>Tunnbröd</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Товар *Tunnbröd* не має постачальника, тому `SupplierName` — `NULL`.
