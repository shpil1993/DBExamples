---
title: Значення NULL
h1: Значення NULL
---

`NULL` означає **відсутність значення**.

Якщо стовпець необов'язковий, можна додати чи змінити запис, не вказуючи значення для нього. Тоді в ньому зберігається `NULL`.

<div class="note" markdown="1">
`NULL` — це не нуль і не порожній рядок `''`. Це особливий маркер «значення невідоме».
</div>

## Як перевірити значення на NULL?

Порівнювати з `NULL` операторами `=`, `<>` **не можна**: результат такого порівняння завжди «невідомо» (UNKNOWN), і рядок не потрапить у результат.

Замість цього використовуйте оператори `IS NULL` та `IS NOT NULL`.

## Синтаксис IS NULL

```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

## Синтаксис IS NOT NULL

```sql
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

## Приклад IS NULL

<div class="example" markdown="1">

Знайти клієнтів, у яких не вказано контактну особу:

```sql
SELECT CustomerName, ContactName, City
FROM Customers
WHERE ContactName IS NULL;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>ContactName</th><th>City</th></tr>
<tr><td>Odesa Seafood</td><td><span class="null">NULL</span></td><td>Odesa</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Приклад IS NOT NULL

<div class="example" markdown="1">

Знайти замовлення, для яких вказано працівника:

```sql
SELECT OrderID, EmployeeID
FROM Orders
WHERE EmployeeID IS NOT NULL;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>EmployeeID</th></tr>
<tr><td>10248</td><td>5</td></tr>
<tr><td>10249</td><td>6</td></tr>
<tr><td>10250</td><td>4</td></tr>
<tr><td>10251</td><td>3</td></tr>
<tr><td>10252</td><td>4</td></tr>
</table></div>
<p class="result-more">… показано 5 з 13 рядків</p>
<!-- run:end -->

</div>

## Чому не працює = NULL

<div class="example" markdown="1">

Цей запит не поверне жодного рядка, хоча клієнт з `ContactName = NULL` існує:

```sql
SELECT CustomerName
FROM Customers
WHERE ContactName = NULL;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
</table></div>
<p class="result-more">Рядків: 0</p>
<!-- run:end -->

</div>

## NULL у виразах

Будь-яка арифметична операція чи конкатенація з `NULL` (через `+`) дає `NULL`:

<div class="example" markdown="1">

```sql
SELECT 10 + NULL AS Sum, N'Text' + NULL AS Concat;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Sum</th><th>Concat</th></tr>
<tr><td><span class="null">NULL</span></td><td><span class="null">NULL</span></td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Щоб замінити `NULL` на інше значення, використовуйте функції `ISNULL()` або `COALESCE()` — див. урок [Функції для NULL](null-functions.html).
