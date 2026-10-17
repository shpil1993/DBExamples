---
title: CASE
h1: Вираз CASE
---

Вираз `CASE` перевіряє умови і повертає значення, коли першу з них виконано (як `if-then-else`).

* Як тільки умова істинна, `CASE` повертає відповідний результат і далі не перевіряє.
* Якщо жодна умова не виконалась, повертається значення з `ELSE`.
* Якщо `ELSE` немає і жодна умова не виконалась — повертається `NULL`.

## Синтаксис (пошуковий CASE)

```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```

## Приклад

<div class="example" markdown="1">

Позначити, чи кількість у рядку замовлення більша за 30:

```sql
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN N'Кількість більша за 30'
    WHEN Quantity = 30 THEN N'Кількість дорівнює 30'
    ELSE N'Кількість менша за 30'
END AS QuantityText
FROM OrderDetails;
```

<!-- run:start rows=6 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>Quantity</th><th>QuantityText</th></tr>
<tr><td>10248</td><td>12</td><td>Кількість менша за 30</td></tr>
<tr><td>10248</td><td>10</td><td>Кількість менша за 30</td></tr>
<tr><td>10248</td><td>5</td><td>Кількість менша за 30</td></tr>
<tr><td>10249</td><td>9</td><td>Кількість менша за 30</td></tr>
<tr><td>10249</td><td>40</td><td>Кількість більша за 30</td></tr>
<tr><td>10250</td><td>10</td><td>Кількість менша за 30</td></tr>
</table></div>
<p class="result-more">… показано 6 з 27 рядків</p>
<!-- run:end -->

</div>

## Простий CASE

Якщо порівнюється одне й те саме значення з кількома варіантами, можна використовувати коротку форму:

```sql
CASE expression
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE result
END
```

<div class="example" markdown="1">

```sql
SELECT CustomerName, Country,
CASE Country
    WHEN N'Ukraine' THEN N'Україна'
    WHEN N'Germany' THEN N'Німеччина'
    WHEN N'France'  THEN N'Франція'
    ELSE N'Інша країна'
END AS CountryUA
FROM Customers;
```

<!-- run:start rows=6 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Country</th><th>CountryUA</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Germany</td><td>Німеччина</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>Mexico</td><td>Інша країна</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>Mexico</td><td>Інша країна</td></tr>
<tr><td>Around the Horn</td><td>UK</td><td>Інша країна</td></tr>
<tr><td>Berglunds snabbköp</td><td>Sweden</td><td>Інша країна</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Germany</td><td>Німеччина</td></tr>
</table></div>
<p class="result-more">… показано 6 з 13 рядків</p>
<!-- run:end -->

</div>

## CASE в ORDER BY

<div class="example" markdown="1">

Відсортувати клієнтів за містом; якщо місто відсутнє — за країною:

```sql
SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th><th>Country</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Berlin</td><td>Germany</td></tr>
<tr><td>Kyiv Market</td><td>Kyiv</td><td>Ukraine</td></tr>
<tr><td>Around the Horn</td><td>London</td><td>UK</td></tr>
<tr><td>Berglunds snabbköp</td><td>Luleå</td><td>Sweden</td></tr>
<tr><td>Lviv Coffee House</td><td>Lviv</td><td>Ukraine</td></tr>
</table></div>
<p class="result-more">… показано 5 з 13 рядків</p>
<!-- run:end -->

</div>

## CASE з агрегатами

`CASE` всередині агрегатної функції дозволяє робити «умовні підрахунки»:

<div class="example" markdown="1">

Кількість дешевих, середніх і дорогих товарів:

```sql
SELECT
    SUM(CASE WHEN Price < 20 THEN 1 ELSE 0 END)               AS Cheap,
    SUM(CASE WHEN Price BETWEEN 20 AND 40 THEN 1 ELSE 0 END)  AS Medium,
    SUM(CASE WHEN Price > 40 THEN 1 ELSE 0 END)               AS Expensive
FROM Products;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Cheap</th><th>Medium</th><th>Expensive</th></tr>
<tr><td>5</td><td>8</td><td>2</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Функція IIF

Для простих умов з двома варіантами в SQL Server є скорочена функція `IIF()`:

<div class="example" markdown="1">

```sql
SELECT ProductName, Price,
       IIF(Price > 30, N'Дорогий', N'Доступний') AS PriceLevel
FROM Products;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th><th>PriceLevel</th></tr>
<tr><td>Chais</td><td>18.00</td><td>Доступний</td></tr>
<tr><td>Chang</td><td>19.00</td><td>Доступний</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td><td>Доступний</td></tr>
<tr><td>Chef Anton's Cajun Seasoning</td><td>22.00</td><td>Доступний</td></tr>
<tr><td>Chef Anton's Gumbo Mix</td><td>21.35</td><td>Доступний</td></tr>
</table></div>
<p class="result-more">… показано 5 з 15 рядків</p>
<!-- run:end -->

</div>

`IIF(умова, значення_якщо_true, значення_якщо_false)` — це скорочений запис `CASE WHEN умова THEN ... ELSE ... END`.
