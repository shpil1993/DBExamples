---
title: MIN() та MAX()
h1: Функції MIN() та MAX()
---

* Функція `MIN()` повертає **найменше** значення вибраного стовпця.
* Функція `MAX()` повертає **найбільше** значення вибраного стовпця.

## Синтаксис

```sql
SELECT MIN(column_name)
FROM table_name
WHERE condition;

SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

## Приклад MIN()

<div class="example" markdown="1">

Знайти найнижчу ціну серед товарів:

```sql
SELECT MIN(Price) AS SmallestPrice
FROM Products;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>SmallestPrice</th></tr>
<tr><td>9.00</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Приклад MAX()

<div class="example" markdown="1">

Знайти найвищу ціну:

```sql
SELECT MAX(Price) AS LargestPrice
FROM Products;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>LargestPrice</th></tr>
<tr><td>97.00</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## MIN() і MAX() для дат і тексту

Функції працюють не лише з числами, а й з датами та рядками:

<div class="example" markdown="1">

Дата першого та останнього замовлення:

```sql
SELECT MIN(OrderDate) AS FirstOrder, MAX(OrderDate) AS LastOrder
FROM Orders;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>FirstOrder</th><th>LastOrder</th></tr>
<tr><td>2024-07-04</td><td>2024-12-02</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Перша і остання назва товару за алфавітом:

```sql
SELECT MIN(ProductName) AS FirstName, MAX(ProductName) AS LastName
FROM Products;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>FirstName</th><th>LastName</th></tr>
<tr><td>Aniseed Syrup</td><td>Vegie-spread</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## MIN() і MAX() з GROUP BY

У поєднанні з [GROUP BY](group-by.html) функції повертають значення для кожної групи:

<div class="example" markdown="1">

Найдешевший і найдорожчий товар у кожній категорії:

```sql
SELECT CategoryID, MIN(Price) AS MinPrice, MAX(Price) AS MaxPrice
FROM Products
GROUP BY CategoryID;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CategoryID</th><th>MinPrice</th><th>MaxPrice</th></tr>
<tr><td>1</td><td>18.00</td><td>19.00</td></tr>
<tr><td>2</td><td>10.00</td><td>43.90</td></tr>
<tr><td>3</td><td>17.45</td><td>17.45</td></tr>
<tr><td>4</td><td>21.00</td><td>38.00</td></tr>
<tr><td>5</td><td>9.00</td><td>9.00</td></tr>
<tr><td>6</td><td>97.00</td><td>97.00</td></tr>
<tr><td>7</td><td>30.00</td><td>30.00</td></tr>
<tr><td>8</td><td>31.00</td><td>31.00</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

## Як знайти весь рядок з мінімальним значенням?

`MIN()` повертає лише саме значення. Щоб отримати весь рядок, можна використати підзапит:

<div class="example" markdown="1">

```sql
SELECT ProductName, Price
FROM Products
WHERE Price = (SELECT MIN(Price) FROM Products);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Tunnbröd</td><td>9.00</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Агрегатні функції `MIN()`, `MAX()`, `SUM()`, `AVG()` та `COUNT(column)` ігнорують значення `NULL`.
</div>
