---
title: "RIGHT JOIN"
h1: "RIGHT JOIN"
---

`RIGHT JOIN` повертає **всі** рядки з правої таблиці (`table2`) і відповідні рядки з лівої таблиці (`table1`). Якщо збігу немає, стовпці лівої таблиці отримують значення `NULL`.

## Синтаксис

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
    ON table1.column_name = table2.column_name;
```

<div class="note" markdown="1">
`RIGHT JOIN` і `RIGHT OUTER JOIN` — одне й те саме.
</div>

## Приклад

<div class="example" markdown="1">

Вибрати всіх працівників і замовлення, які вони оформили (якщо такі є):

```sql
SELECT o.OrderID, e.LastName, e.FirstName
FROM Orders AS o
RIGHT JOIN Employees AS e ON o.EmployeeID = e.EmployeeID
ORDER BY o.OrderID;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>LastName</th><th>FirstName</th></tr>
<tr><td><span class="null">NULL</span></td><td>Fuller</td><td>Andrew</td></tr>
<tr><td>10248</td><td>Buchanan</td><td>Steven</td></tr>
<tr><td>10249</td><td>Suyama</td><td>Michael</td></tr>
<tr><td>10250</td><td>Peacock</td><td>Margaret</td></tr>
<tr><td>10251</td><td>Leverling</td><td>Janet</td></tr>
<tr><td>10252</td><td>Peacock</td><td>Margaret</td></tr>
<tr><td>10253</td><td>Leverling</td><td>Janet</td></tr>
<tr><td>10254</td><td>Peacock</td><td>Margaret</td></tr>
<tr><td>10255</td><td>Peacock</td><td>Margaret</td></tr>
<tr><td>10256</td><td>Leverling</td><td>Janet</td></tr>
<tr><td>10257</td><td>Davolio</td><td>Nancy</td></tr>
<tr><td>10258</td><td>Davolio</td><td>Nancy</td></tr>
<tr><td>10259</td><td>King</td><td>Robert</td></tr>
<tr><td>10260</td><td>Davolio</td><td>Nancy</td></tr>
</table></div>
<p class="result-more">Рядків: 14</p>
<!-- run:end -->

</div>

Працівник *Andrew Fuller* не оформив жодного замовлення, тому `OrderID` для нього — `NULL`. Значення `NULL` при сортуванні йдуть першими.

## RIGHT JOIN чи LEFT JOIN?

Будь-який `RIGHT JOIN` можна переписати як `LEFT JOIN`, помінявши таблиці місцями. Наступний запит повертає той самий результат:

```sql
SELECT o.OrderID, e.LastName, e.FirstName
FROM Employees AS e
LEFT JOIN Orders AS o ON o.EmployeeID = e.EmployeeID
ORDER BY o.OrderID;
```

На практиці частіше використовують `LEFT JOIN` — такі запити легше читати.
