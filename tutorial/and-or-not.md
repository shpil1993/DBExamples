---
title: "AND, OR, NOT"
h1: "Оператори AND, OR та NOT"
---

Умову `WHERE` можна поєднувати з операторами `AND`, `OR` та `NOT`.

* `AND` — повертає рядок, якщо **всі** умови істинні.
* `OR` — повертає рядок, якщо **хоча б одна** з умов істинна.
* `NOT` — повертає рядок, якщо умова **хибна**.

## Синтаксис AND

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

<div class="example" markdown="1">

Вибрати клієнтів з Німеччини, що знаходяться в Берліні:

```sql
SELECT * FROM Customers
WHERE Country = N'Germany' AND City = N'Berlin';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>ContactName</th><th>Address</th><th>City</th><th>PostalCode</th><th>Country</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Obere Str. 57</td><td>Berlin</td><td>12209</td><td>Germany</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Синтаксис OR

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

<div class="example" markdown="1">

Вибрати клієнтів з Німеччини або Іспанії:

```sql
SELECT CustomerName, City, Country
FROM Customers
WHERE Country = N'Germany' OR Country = N'Spain';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th><th>Country</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Berlin</td><td>Germany</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Mannheim</td><td>Germany</td></tr>
<tr><td>Bólido Comidas preparadas</td><td>Madrid</td><td>Spain</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## Синтаксис NOT

```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

<div class="example" markdown="1">

Вибрати клієнтів не з Мексики:

```sql
SELECT CustomerName, Country
FROM Customers
WHERE NOT Country = N'Mexico';
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Country</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Germany</td></tr>
<tr><td>Around the Horn</td><td>UK</td></tr>
<tr><td>Berglunds snabbköp</td><td>Sweden</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Germany</td></tr>
<tr><td>Blondel père et fils</td><td>France</td></tr>
</table></div>
<p class="result-more">… показано 5 з 11 рядків</p>
<!-- run:end -->

</div>

`NOT` можна поєднувати з іншими операторами: `NOT LIKE`, `NOT BETWEEN`, `NOT IN`, `IS NOT NULL`.

## Поєднання AND, OR і NOT

Оператор `AND` має вищий пріоритет, ніж `OR`. Використовуйте **дужки**, щоб явно задати порядок обчислення.

<div class="example" markdown="1">

Вибрати клієнтів з Німеччини, які знаходяться в Берліні **або** Мангеймі:

```sql
SELECT CustomerName, City, Country
FROM Customers
WHERE Country = N'Germany' AND (City = N'Berlin' OR City = N'Mannheim');
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th><th>Country</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Berlin</td><td>Germany</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Mannheim</td><td>Germany</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Вибрати клієнтів, які не з Німеччини і не з Мексики:

```sql
SELECT CustomerName, Country
FROM Customers
WHERE NOT Country = N'Germany' AND NOT Country = N'Mexico';
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Country</th></tr>
<tr><td>Around the Horn</td><td>UK</td></tr>
<tr><td>Berglunds snabbköp</td><td>Sweden</td></tr>
<tr><td>Blondel père et fils</td><td>France</td></tr>
<tr><td>Bólido Comidas preparadas</td><td>Spain</td></tr>
<tr><td>Bon app'</td><td>France</td></tr>
</table></div>
<p class="result-more">… показано 5 з 9 рядків</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
Без дужок умова `A AND B OR C` читається як `(A AND B) OR C`. Це поширене джерело помилок — ставте дужки, якщо сумніваєтеся.
</div>
