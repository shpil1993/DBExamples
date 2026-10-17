---
title: "BETWEEN"
h1: "Оператор BETWEEN"
---

Оператор `BETWEEN` вибирає значення в заданому **діапазоні**. Значеннями можуть бути числа, текст або дати.

`BETWEEN` є **включним**: початкове та кінцеве значення входять у діапазон.

## Синтаксис

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

## Приклад

<div class="example" markdown="1">

Товари з ціною від 10 до 20:

```sql
SELECT ProductName, Price FROM Products
WHERE Price BETWEEN 10 AND 20;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Chais</td><td>18.00</td></tr>
<tr><td>Chang</td><td>19.00</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td></tr>
<tr><td>Pavlova</td><td>17.45</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>

Запис `Price BETWEEN 10 AND 20` еквівалентний `Price >= 10 AND Price <= 20`.

## NOT BETWEEN

<div class="example" markdown="1">

Товари з ціною поза діапазоном від 10 до 40:

```sql
SELECT ProductName, Price FROM Products
WHERE Price NOT BETWEEN 10 AND 40;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>Vegie-spread</td><td>43.90</td></tr>
<tr><td>Tunnbröd</td><td>9.00</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## BETWEEN з IN

<div class="example" markdown="1">

Товари з ціною від 10 до 20, які не належать до категорій 1 і 2:

```sql
SELECT ProductName, Price, CategoryID FROM Products
WHERE Price BETWEEN 10 AND 20
  AND CategoryID NOT IN (1, 2);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th><th>CategoryID</th></tr>
<tr><td>Pavlova</td><td>17.45</td><td>3</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## BETWEEN з текстовими значеннями

<div class="example" markdown="1">

Товари, назви яких за алфавітом знаходяться між «Chais» і «Ikura»:

```sql
SELECT ProductName FROM Products
WHERE ProductName BETWEEN N'Chais' AND N'Ikura'
ORDER BY ProductName;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th></tr>
<tr><td>Chais</td></tr>
<tr><td>Chang</td></tr>
<tr><td>Chef Anton's Cajun Seasoning</td></tr>
<tr><td>Chef Anton's Gumbo Mix</td></tr>
<tr><td>Grandma's Boysenberry Spread</td></tr>
<tr><td>Ikura</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

## BETWEEN з датами

<div class="example" markdown="1">

Замовлення за липень 2024 року:

```sql
SELECT OrderID, OrderDate FROM Orders
WHERE OrderDate BETWEEN '2024-07-01' AND '2024-07-31';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>OrderDate</th></tr>
<tr><td>10248</td><td>2024-07-04</td></tr>
<tr><td>10249</td><td>2024-07-05</td></tr>
<tr><td>10250</td><td>2024-07-08</td></tr>
<tr><td>10251</td><td>2024-07-08</td></tr>
<tr><td>10252</td><td>2024-07-09</td></tr>
<tr><td>10253</td><td>2024-07-10</td></tr>
<tr><td>10254</td><td>2024-07-11</td></tr>
<tr><td>10255</td><td>2024-07-12</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
**Обережно з датою й часом.** Якщо стовпець має тип `DATETIME` (з часом), то `BETWEEN '2024-07-01' AND '2024-07-31'` **не включить** записи 31 липня після 00:00. Для таких стовпців надійніше писати півінтервал:

```sql
WHERE OrderDate >= '2024-07-01' AND OrderDate < '2024-08-01'
```
</div>
