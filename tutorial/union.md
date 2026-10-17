---
title: UNION
h1: Оператор UNION
---

Оператор `UNION` об'єднує результати двох або більше інструкцій `SELECT`.

Вимоги:

* кожен `SELECT` повинен мати **однакову кількість** стовпців;
* стовпці повинні мати **сумісні типи даних**;
* стовпці мають іти в **однаковому порядку**.

## Синтаксис UNION

```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

`UNION` повертає лише **різні** значення (видаляє дублікати). Щоб залишити дублікати, використовуйте `UNION ALL`:

```sql
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
```

<div class="note" markdown="1">
Імена стовпців результату беруться з першого `SELECT`.
</div>

## Приклад UNION

<div class="example" markdown="1">

Різні країни клієнтів і постачальників:

```sql
SELECT Country FROM Customers
UNION
SELECT Country FROM Suppliers
ORDER BY Country;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th></tr>
<tr><td>Australia</td></tr>
<tr><td>Canada</td></tr>
<tr><td>France</td></tr>
<tr><td>Germany</td></tr>
<tr><td>Japan</td></tr>
<tr><td>Mexico</td></tr>
<tr><td>Spain</td></tr>
<tr><td>Sweden</td></tr>
<tr><td>UK</td></tr>
<tr><td>Ukraine</td></tr>
<tr><td>USA</td></tr>
</table></div>
<p class="result-more">Рядків: 11</p>
<!-- run:end -->

</div>

## Приклад UNION ALL

<div class="example" markdown="1">

Країни клієнтів і постачальників **з повтореннями**:

```sql
SELECT Country FROM Customers
UNION ALL
SELECT Country FROM Suppliers
ORDER BY Country;
```

<!-- run:start rows=8 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th></tr>
<tr><td>Australia</td></tr>
<tr><td>Canada</td></tr>
<tr><td>France</td></tr>
<tr><td>France</td></tr>
<tr><td>Germany</td></tr>
<tr><td>Germany</td></tr>
<tr><td>Japan</td></tr>
<tr><td>Mexico</td></tr>
</table></div>
<p class="result-more">… показано 8 з 19 рядків</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
`UNION ALL` працює швидше за `UNION`, бо не потребує пошуку дублікатів. Якщо ви знаєте, що дублікатів немає або вони потрібні, використовуйте `UNION ALL`.
</div>

## UNION з WHERE

<div class="example" markdown="1">

Міста клієнтів і постачальників з Великої Британії та США:

```sql
SELECT City, Country FROM Customers
WHERE Country IN (N'UK', N'USA')
UNION
SELECT City, Country FROM Suppliers
WHERE Country IN (N'UK', N'USA')
ORDER BY City;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>City</th><th>Country</th></tr>
<tr><td>Ann Arbor</td><td>USA</td></tr>
<tr><td>London</td><td>UK</td></tr>
<tr><td>New Orleans</td><td>USA</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## Додатковий стовпець-мітка

<div class="example" markdown="1">

Список усіх контактних осіб клієнтів і постачальників з типом:

```sql
SELECT N'Customer' AS Type, ContactName, City, Country
FROM Customers
UNION
SELECT N'Supplier', ContactName, City, Country
FROM Suppliers;
```

<!-- run:start rows=6 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Type</th><th>ContactName</th><th>City</th><th>Country</th></tr>
<tr><td>Customer</td><td><span class="null">NULL</span></td><td>Odesa</td><td>Ukraine</td></tr>
<tr><td>Customer</td><td>Ana Trujillo</td><td>México D.F.</td><td>Mexico</td></tr>
<tr><td>Customer</td><td>Antonio Moreno</td><td>México D.F.</td><td>Mexico</td></tr>
<tr><td>Customer</td><td>Christina Berglund</td><td>Luleå</td><td>Sweden</td></tr>
<tr><td>Customer</td><td>Elizabeth Lincoln</td><td>Tsawassen</td><td>Canada</td></tr>
<tr><td>Customer</td><td>Frédérique Citeaux</td><td>Strasbourg</td><td>France</td></tr>
</table></div>
<p class="result-more">… показано 6 з 19 рядків</p>
<!-- run:end -->

</div>

## INTERSECT та EXCEPT

SQL Server підтримує ще два оператори над множинами:

* `INTERSECT` — рядки, що є **в обох** результатах;
* `EXCEPT` — рядки з першого результату, яких **немає** в другому.

<div class="example" markdown="1">

Країни, у яких є і клієнти, і постачальники:

```sql
SELECT Country FROM Customers
INTERSECT
SELECT Country FROM Suppliers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th></tr>
<tr><td>Spain</td></tr>
<tr><td>UK</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Країни клієнтів, у яких немає постачальників:

```sql
SELECT Country FROM Customers
EXCEPT
SELECT Country FROM Suppliers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th></tr>
<tr><td>Canada</td></tr>
<tr><td>France</td></tr>
<tr><td>Germany</td></tr>
<tr><td>Mexico</td></tr>
<tr><td>Sweden</td></tr>
<tr><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>
