---
title: IN
h1: Оператор IN
---

Оператор `IN` дає змогу вказати в умові `WHERE` **кілька значень**.

`IN` — це скорочений запис для кількох умов `OR`.

## Синтаксис

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

або з підзапитом:

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);
```

## Приклад

<div class="example" markdown="1">

Клієнти з Німеччини, Франції або Великої Британії:

```sql
SELECT CustomerName, Country FROM Customers
WHERE Country IN (N'Germany', N'France', N'UK');
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Country</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Germany</td></tr>
<tr><td>Around the Horn</td><td>UK</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Germany</td></tr>
<tr><td>Blondel père et fils</td><td>France</td></tr>
<tr><td>Bon app'</td><td>France</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

Цей запит еквівалентний такому:

```sql
SELECT CustomerName, Country FROM Customers
WHERE Country = N'Germany' OR Country = N'France' OR Country = N'UK';
```

## NOT IN

<div class="example" markdown="1">

Клієнти, які **не** з Німеччини, Франції чи Великої Британії:

```sql
SELECT CustomerName, Country FROM Customers
WHERE Country NOT IN (N'Germany', N'France', N'UK');
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Country</th></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>Mexico</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>Mexico</td></tr>
<tr><td>Berglunds snabbköp</td><td>Sweden</td></tr>
<tr><td>Bólido Comidas preparadas</td><td>Spain</td></tr>
<tr><td>Bottom-Dollar Marketse</td><td>Canada</td></tr>
<tr><td>Kyiv Market</td><td>Ukraine</td></tr>
<tr><td>Lviv Coffee House</td><td>Ukraine</td></tr>
<tr><td>Odesa Seafood</td><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

## IN з підзапитом

<div class="example" markdown="1">

Клієнти, які мають хоча б одне замовлення:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);
```

<!-- run:start rows=12 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Alfreds Futterkiste</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td></tr>
<tr><td>Antonio Moreno Taquería</td></tr>
<tr><td>Around the Horn</td></tr>
<tr><td>Berglunds snabbköp</td></tr>
<tr><td>Blondel père et fils</td></tr>
<tr><td>Bólido Comidas preparadas</td></tr>
<tr><td>Bon app'</td></tr>
<tr><td>Bottom-Dollar Marketse</td></tr>
<tr><td>Kyiv Market</td></tr>
<tr><td>Lviv Coffee House</td></tr>
</table></div>
<p class="result-more">Рядків: 11</p>
<!-- run:end -->

</div>

## NOT IN з підзапитом

<div class="example" markdown="1">

Клієнти, у яких немає жодного замовлення:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);
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

<div class="warn" markdown="1">
**Пастка NOT IN і NULL.** Якщо підзапит у `NOT IN` повертає хоча б одне значення `NULL`, весь запит поверне **порожній** результат. У таблиці `Orders` стовпець `CustomerID` допускає `NULL`, тому надійніше використовувати `NOT EXISTS` (див. урок [EXISTS](exists.html)) або додати в підзапит `WHERE CustomerID IS NOT NULL`.
</div>
