---
title: "LEFT JOIN"
h1: "LEFT JOIN"
---

`LEFT JOIN` повертає **всі** рядки з лівої таблиці (`table1`) і відповідні рядки з правої таблиці (`table2`). Якщо збігу немає, стовпці правої таблиці отримують значення `NULL`.

## Синтаксис

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
    ON table1.column_name = table2.column_name;
```

<div class="note" markdown="1">
`LEFT JOIN` і `LEFT OUTER JOIN` — одне й те саме.
</div>

## Приклад

<div class="example" markdown="1">

Вибрати всіх клієнтів і їхні замовлення (якщо є):

```sql
SELECT c.CustomerName, o.OrderID
FROM Customers AS c
LEFT JOIN Orders AS o ON c.CustomerID = o.CustomerID
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

Клієнти без замовлень (*Blauer See Delikatessen*, *Odesa Seafood*) теж потрапили в результат — з `OrderID = NULL`.

## Пошук рядків без збігу

Поширений прийом: `LEFT JOIN` + перевірка `IS NULL` у правій таблиці. Так знаходять записи, для яких **немає** пов'язаних даних.

<div class="example" markdown="1">

Клієнти, які ще не зробили жодного замовлення:

```sql
SELECT c.CustomerName
FROM Customers AS c
LEFT JOIN Orders AS o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Blauer See Delikatessen</td></tr>
<tr><td>Odesa Seafood</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Умова в ON проти умови в WHERE

Для `LEFT JOIN` важливо, де стоїть умова:

* умова в `ON` впливає лише на те, **які рядки правої таблиці** приєднуються;
* умова в `WHERE` фільтрує **весь результат**.

<div class="example" markdown="1">

Усі клієнти з України та їхні замовлення, зроблені у вересні 2024 року:

```sql
SELECT c.CustomerName, o.OrderID, o.OrderDate
FROM Customers AS c
LEFT JOIN Orders AS o
    ON  c.CustomerID = o.CustomerID
    AND o.OrderDate >= '2024-09-01' AND o.OrderDate < '2024-10-01'
WHERE c.Country = N'Ukraine';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>OrderID</th><th>OrderDate</th></tr>
<tr><td>Kyiv Market</td><td>10257</td><td>2024-09-01</td></tr>
<tr><td>Kyiv Market</td><td>10258</td><td>2024-09-20</td></tr>
<tr><td>Lviv Coffee House</td><td><span class="null">NULL</span></td><td><span class="null">NULL</span></td></tr>
<tr><td>Odesa Seafood</td><td><span class="null">NULL</span></td><td><span class="null">NULL</span></td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>
