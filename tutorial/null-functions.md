---
title: "Функції для NULL"
h1: "Функції ISNULL(), COALESCE() та NULLIF()"
---

Значення `NULL` у виразах часто дає небажаний результат. SQL Server має функції, які допомагають з ним працювати.

## Проблема

Припустимо, у таблиці `Products` є стовпці `UnitsInStock` та `UnitsOnOrder`, і другий з них може містити `NULL`. Тоді вираз

```sql
SELECT ProductName, Price * (UnitsInStock + UnitsOnOrder)
FROM Products;
```

поверне `NULL` для кожного товару, де `UnitsOnOrder` дорівнює `NULL` — бо будь-яка арифметика з `NULL` дає `NULL`.

Розгляньмо це на нашій демо-базі: у таблиці `Customers` у одного клієнта немає контактної особи.

<div class="example" markdown="1">

```sql
SELECT CustomerName, N'Контакт: ' + ContactName AS Contact
FROM Customers
WHERE Country = N'Ukraine';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Contact</th></tr>
<tr><td>Kyiv Market</td><td>Контакт: Olena Shevchenko</td></tr>
<tr><td>Lviv Coffee House</td><td>Контакт: Taras Kovalenko</td></tr>
<tr><td>Odesa Seafood</td><td><span class="null">NULL</span></td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## ISNULL()

`ISNULL(вираз, заміна)` повертає `заміну`, якщо `вираз` дорівнює `NULL`:

<div class="example" markdown="1">

```sql
SELECT CustomerName,
       N'Контакт: ' + ISNULL(ContactName, N'не вказано') AS Contact
FROM Customers
WHERE Country = N'Ukraine';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>Contact</th></tr>
<tr><td>Kyiv Market</td><td>Контакт: Olena Shevchenko</td></tr>
<tr><td>Lviv Coffee House</td><td>Контакт: Taras Kovalenko</td></tr>
<tr><td>Odesa Seafood</td><td>Контакт: не вказано</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
У MySQL аналогічна функція називається `IFNULL()`, а в SQL Server функції `IFNULL()` немає.
</div>

## COALESCE()

`COALESCE(вираз1, вираз2, ...)` повертає **перше** значення зі списку, яке не є `NULL`. Ця функція входить у стандарт SQL і працює майже в усіх СУБД.

<div class="example" markdown="1">

```sql
SELECT CustomerName,
       COALESCE(ContactName, CustomerName, N'—') AS DisplayName
FROM Customers
WHERE Country = N'Ukraine';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>DisplayName</th></tr>
<tr><td>Kyiv Market</td><td>Olena Shevchenko</td></tr>
<tr><td>Lviv Coffee House</td><td>Taras Kovalenko</td></tr>
<tr><td>Odesa Seafood</td><td>Odesa Seafood</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Працівник замовлення або 0, якщо працівника не вказано:

```sql
SELECT OrderID, COALESCE(EmployeeID, 0) AS EmployeeID
FROM Orders
WHERE OrderID > 10258;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>EmployeeID</th></tr>
<tr><td>10259</td><td>7</td></tr>
<tr><td>10260</td><td>2</td></tr>
<tr><td>10261</td><td>0</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

### ISNULL чи COALESCE?

| | `ISNULL` | `COALESCE` |
|---|---|---|
| Кількість аргументів | Рівно 2 | 2 і більше |
| Стандарт SQL | Ні (лише SQL Server) | Так |
| Тип результату | Тип **першого** аргументу | Тип з найвищим пріоритетом серед аргументів |

<div class="warn" markdown="1">
Через правило типів `ISNULL` може обрізати рядок: якщо перший аргумент має тип `VARCHAR(5)`, то й заміна буде обрізана до 5 символів.
</div>

## NULLIF()

`NULLIF(вираз1, вираз2)` повертає `NULL`, якщо вирази **рівні**, інакше — `вираз1`.

Типове використання — захист від ділення на нуль:

<div class="example" markdown="1">

```sql
SELECT 100 / NULLIF(0, 0) AS SafeDivision;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>SafeDivision</th></tr>
<tr><td><span class="null">NULL</span></td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Без `NULLIF` вираз `100 / 0` викликав би помилку *Divide by zero error encountered*.
