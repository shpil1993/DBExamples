---
title: "SELECT DISTINCT"
h1: "Інструкція SELECT DISTINCT"
---

Інструкція `SELECT DISTINCT` повертає лише **унікальні** (різні) значення.

У таблиці стовпець часто містить повторювані значення. Якщо потрібен лише перелік різних значень, використовуйте `DISTINCT`.

## Синтаксис

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

## Приклад без DISTINCT

<div class="example" markdown="1">

Вибрати країни всіх клієнтів (з повтореннями):

```sql
SELECT Country FROM Customers;
```

<!-- run:start rows=13 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th></tr>
<tr><td>Germany</td></tr>
<tr><td>Mexico</td></tr>
<tr><td>Mexico</td></tr>
<tr><td>UK</td></tr>
<tr><td>Sweden</td></tr>
<tr><td>Germany</td></tr>
<tr><td>France</td></tr>
<tr><td>Spain</td></tr>
<tr><td>France</td></tr>
<tr><td>Canada</td></tr>
<tr><td>Ukraine</td></tr>
<tr><td>Ukraine</td></tr>
<tr><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 13</p>
<!-- run:end -->

</div>

## Приклад із DISTINCT

<div class="example" markdown="1">

Вибрати лише різні країни клієнтів:

```sql
SELECT DISTINCT Country FROM Customers;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th></tr>
<tr><td>Canada</td></tr>
<tr><td>France</td></tr>
<tr><td>Germany</td></tr>
<tr><td>Mexico</td></tr>
<tr><td>Spain</td></tr>
<tr><td>Sweden</td></tr>
<tr><td>UK</td></tr>
<tr><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

## DISTINCT для кількох стовпців

Якщо вказати кілька стовпців, унікальною вважається **комбінація** значень:

<div class="example" markdown="1">

```sql
SELECT DISTINCT Country, City
FROM Customers
ORDER BY Country;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Country</th><th>City</th></tr>
<tr><td>Canada</td><td>Tsawassen</td></tr>
<tr><td>France</td><td>Marseille</td></tr>
<tr><td>France</td><td>Strasbourg</td></tr>
<tr><td>Germany</td><td>Berlin</td></tr>
<tr><td>Germany</td><td>Mannheim</td></tr>
<tr><td>Mexico</td><td>México D.F.</td></tr>
<tr><td>Spain</td><td>Madrid</td></tr>
<tr><td>Sweden</td><td>Luleå</td></tr>
<tr><td>UK</td><td>London</td></tr>
<tr><td>Ukraine</td><td>Kyiv</td></tr>
<tr><td>Ukraine</td><td>Lviv</td></tr>
<tr><td>Ukraine</td><td>Odesa</td></tr>
</table></div>
<p class="result-more">Рядків: 12</p>
<!-- run:end -->

</div>

## Підрахунок різних значень

Щоб порахувати кількість різних значень, використовуйте `COUNT(DISTINCT ...)`:

<div class="example" markdown="1">

```sql
SELECT COUNT(DISTINCT Country) AS CountryCount
FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CountryCount</th></tr>
<tr><td>8</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
`DISTINCT` вважає всі значення `NULL` однаковими: у результаті буде не більше одного рядка з `NULL`. Водночас `COUNT(DISTINCT ...)` значення `NULL` не враховує.
</div>
