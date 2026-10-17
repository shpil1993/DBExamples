---
title: "WHERE"
h1: "Умова WHERE"
---

Умова `WHERE` використовується для фільтрації записів.

Вона дає змогу отримати лише ті рядки, які відповідають заданій умові.

## Синтаксис

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

<div class="note" markdown="1">
`WHERE` використовується не лише в `SELECT`, а й в інструкціях `UPDATE`, `DELETE` тощо.
</div>

## Приклад

<div class="example" markdown="1">

Вибрати всіх клієнтів з Мексики:

```sql
SELECT * FROM Customers
WHERE Country = N'Mexico';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>ContactName</th><th>Address</th><th>City</th><th>PostalCode</th><th>Country</th></tr>
<tr><td>2</td><td>Ana Trujillo Emparedados y helados</td><td>Ana Trujillo</td><td>Avda. de la Constitución 2222</td><td>México D.F.</td><td>05021</td><td>Mexico</td></tr>
<tr><td>3</td><td>Antonio Moreno Taquería</td><td>Antonio Moreno</td><td>Mataderos 2312</td><td>México D.F.</td><td>05023</td><td>Mexico</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Текстові та числові значення

Текстові значення беруться в **одинарні лапки**. Числові значення лапок не потребують:

<div class="example" markdown="1">

```sql
SELECT * FROM Customers
WHERE CustomerID = 1;
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

<div class="warn" markdown="1">
У T-SQL рядки беруться саме в одинарні лапки `'...'`. Подвійні лапки `"..."` за замовчуванням позначають **імена** об'єктів (як і квадратні дужки `[...]`), а не текст.

Щоб записати апостроф усередині рядка, подвойте його: `N'Bon app'''`.
</div>

## Оператори в WHERE

| Оператор | Опис |
|---|---|
| `=` | Дорівнює |
| `>` | Більше |
| `<` | Менше |
| `>=` | Більше або дорівнює |
| `<=` | Менше або дорівнює |
| `<>` або `!=` | Не дорівнює |
| `BETWEEN` | У межах діапазону |
| `LIKE` | Відповідає шаблону |
| `IN` | Одне з кількох значень |
| `IS NULL` | Значення відсутнє |

<div class="example" markdown="1">

Вибрати товари, дорожчі за 30:

```sql
SELECT ProductName, Price
FROM Products
WHERE Price > 30;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>40.00</td></tr>
<tr><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>Ikura</td><td>31.00</td></tr>
<tr><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
<tr><td>Vegie-spread</td><td>43.90</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Вибрати замовлення, зроблені після 1 вересня 2024 року:

```sql
SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE OrderDate >= '2024-09-01';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerID</th><th>OrderDate</th></tr>
<tr><td>10257</td><td>11</td><td>2024-09-01</td></tr>
<tr><td>10258</td><td>11</td><td>2024-09-20</td></tr>
<tr><td>10259</td><td>12</td><td>2024-10-03</td></tr>
<tr><td>10260</td><td>1</td><td>2024-11-14</td></tr>
<tr><td>10261</td><td>10</td><td>2024-12-02</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Дати рекомендується записувати у форматі `'YYYY-MM-DD'` (або `'YYYYMMDD'`) — так SQL Server однаково розуміє їх незалежно від мовних налаштувань.
</div>
