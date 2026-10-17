---
title: "CTE та віконні функції"
h1: "CTE та віконні функції"
---

## Загальні табличні вирази (CTE)

**CTE** (Common Table Expression) — це іменований тимчасовий результат запиту, який існує лише в межах однієї інструкції. CTE робить складні запити читабельнішими.

```sql
WITH cte_name (column1, column2, ...) AS (
    SELECT ...
)
SELECT ... FROM cte_name;
```

<div class="example" markdown="1">

Суми замовлень і ті замовлення, що більші за середню суму:

```sql
WITH OrderSums AS (
    SELECT od.OrderID, SUM(od.Quantity * p.Price) AS Total
    FROM OrderDetails AS od
    JOIN Products AS p ON p.ProductID = od.ProductID
    GROUP BY od.OrderID
)
SELECT OrderID, Total
FROM OrderSums
WHERE Total > (SELECT AVG(Total) FROM OrderSums)
ORDER BY Total DESC;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>Total</th></tr>
<tr><td>10253</td><td>2120.00</td></tr>
<tr><td>10255</td><td>1652.25</td></tr>
<tr><td>10248</td><td>1441.50</td></tr>
<tr><td>10250</td><td>1310.00</td></tr>
<tr><td>10257</td><td>1032.00</td></tr>
<tr><td>10252</td><td>1025.00</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Якщо перед `WITH` є інша інструкція, вона повинна закінчуватися крапкою з комою. Тому часто пишуть `;WITH ...`.
</div>

### Кілька CTE

```sql
WITH
CustomersUA AS (
    SELECT CustomerID, CustomerName FROM Customers WHERE Country = N'Ukraine'
),
OrdersUA AS (
    SELECT o.OrderID, c.CustomerName
    FROM Orders o JOIN CustomersUA c ON c.CustomerID = o.CustomerID
)
SELECT * FROM OrdersUA;
```

### Рекурсивний CTE

Рекурсивний CTE посилається сам на себе. Він ідеально підходить для ієрархій — наприклад, структури підпорядкування працівників:

<div class="example" markdown="1">

```sql
WITH Hierarchy AS (
    -- якір: керівник верхнього рівня
    SELECT EmployeeID, FirstName, LastName, ManagerID, 0 AS Level
    FROM Employees
    WHERE ManagerID IS NULL

    UNION ALL

    -- рекурсивна частина: підлеглі
    SELECT e.EmployeeID, e.FirstName, e.LastName, e.ManagerID, h.Level + 1
    FROM Employees AS e
    JOIN Hierarchy AS h ON e.ManagerID = h.EmployeeID
)
SELECT REPLICATE(N'    ', Level) + FirstName + N' ' + LastName AS Employee, Level
FROM Hierarchy
ORDER BY Level, LastName;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Employee</th><th>Level</th></tr>
<tr><td>Andrew Fuller</td><td>0</td></tr>
<tr><td>    Steven Buchanan</td><td>1</td></tr>
<tr><td>    Nancy Davolio</td><td>1</td></tr>
<tr><td>    Janet Leverling</td><td>1</td></tr>
<tr><td>    Margaret Peacock</td><td>1</td></tr>
<tr><td>        Robert King</td><td>2</td></tr>
<tr><td>        Michael Suyama</td><td>2</td></tr>
</table></div>
<p class="result-more">Рядків: 7</p>
<!-- run:end -->

</div>

## Віконні функції

**Віконні функції** обчислюють значення на основі набору рядків («вікна»), пов'язаних з поточним рядком, але, на відміну від `GROUP BY`, **не згортають** рядки в один.

```sql
function_name(...) OVER (
    [PARTITION BY column(s)]
    [ORDER BY column(s)]
)
```

* `PARTITION BY` ділить рядки на групи (вікна);
* `ORDER BY` задає порядок рядків у вікні.

### Функції ранжування

| Функція | Опис |
|---|---|
| `ROW_NUMBER()` | Послідовний номер рядка: 1, 2, 3, 4 |
| `RANK()` | Ранг з пропусками при однакових значеннях: 1, 2, 2, 4 |
| `DENSE_RANK()` | Ранг без пропусків: 1, 2, 2, 3 |
| `NTILE(n)` | Ділить рядки на n приблизно рівних груп |

<div class="example" markdown="1">

Нумерація товарів за ціною в межах кожної категорії:

```sql
SELECT CategoryID, ProductName, Price,
       ROW_NUMBER() OVER (PARTITION BY CategoryID ORDER BY Price DESC) AS RowNum
FROM Products
WHERE CategoryID IN (2, 4);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CategoryID</th><th>ProductName</th><th>Price</th><th>RowNum</th></tr>
<tr><td>2</td><td>Vegie-spread</td><td>43.90</td><td>1</td></tr>
<tr><td>2</td><td>Northwoods Cranberry Sauce</td><td>40.00</td><td>2</td></tr>
<tr><td>2</td><td>Grandma's Boysenberry Spread</td><td>25.00</td><td>3</td></tr>
<tr><td>2</td><td>Chef Anton's Cajun Seasoning</td><td>22.00</td><td>4</td></tr>
<tr><td>2</td><td>Chef Anton's Gumbo Mix</td><td>21.35</td><td>5</td></tr>
<tr><td>2</td><td>Aniseed Syrup</td><td>10.00</td><td>6</td></tr>
<tr><td>4</td><td>Queso Manchego La Pastora</td><td>38.00</td><td>1</td></tr>
<tr><td>4</td><td>Queso Cabrales</td><td>21.00</td><td>2</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Найдорожчий товар у кожній категорії (типовий прийом з CTE + `ROW_NUMBER`):

```sql
WITH Ranked AS (
    SELECT CategoryID, ProductName, Price,
           ROW_NUMBER() OVER (PARTITION BY CategoryID ORDER BY Price DESC) AS rn
    FROM Products
)
SELECT CategoryID, ProductName, Price
FROM Ranked
WHERE rn = 1;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CategoryID</th><th>ProductName</th><th>Price</th></tr>
<tr><td>1</td><td>Chang</td><td>19.00</td></tr>
<tr><td>2</td><td>Vegie-spread</td><td>43.90</td></tr>
<tr><td>3</td><td>Pavlova</td><td>17.45</td></tr>
<tr><td>4</td><td>Queso Manchego La Pastora</td><td>38.00</td></tr>
<tr><td>5</td><td>Tunnbröd</td><td>9.00</td></tr>
<tr><td>6</td><td>Mishi Kobe Niku</td><td>97.00</td></tr>
<tr><td>7</td><td>Uncle Bob's Organic Dried Pears</td><td>30.00</td></tr>
<tr><td>8</td><td>Ikura</td><td>31.00</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

</div>

### Агрегатні віконні функції

Звичайні агрегатні функції (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`) теж можна використовувати з `OVER`:

<div class="example" markdown="1">

Ціна товару порівняно із середньою ціною в його категорії:

```sql
SELECT ProductName, CategoryID, Price,
       AVG(Price) OVER (PARTITION BY CategoryID) AS CategoryAvg,
       Price - AVG(Price) OVER (PARTITION BY CategoryID) AS Diff
FROM Products
WHERE CategoryID = 2;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>CategoryID</th><th>Price</th><th>CategoryAvg</th><th>Diff</th></tr>
<tr><td>Aniseed Syrup</td><td>2</td><td>10.00</td><td>27.041666</td><td>-17.041666</td></tr>
<tr><td>Chef Anton's Cajun Seasoning</td><td>2</td><td>22.00</td><td>27.041666</td><td>-5.041666</td></tr>
<tr><td>Chef Anton's Gumbo Mix</td><td>2</td><td>21.35</td><td>27.041666</td><td>-5.691666</td></tr>
<tr><td>Grandma's Boysenberry Spread</td><td>2</td><td>25.00</td><td>27.041666</td><td>-2.041666</td></tr>
<tr><td>Northwoods Cranberry Sauce</td><td>2</td><td>40.00</td><td>27.041666</td><td>12.958334</td></tr>
<tr><td>Vegie-spread</td><td>2</td><td>43.90</td><td>27.041666</td><td>16.858334</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Наростаючий підсумок кількості замовлень за датою:

```sql
SELECT OrderID, OrderDate,
       COUNT(*) OVER (ORDER BY OrderDate, OrderID
                      ROWS UNBOUNDED PRECEDING) AS RunningCount
FROM Orders;
```

<!-- run:start rows=6 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>OrderDate</th><th>RunningCount</th></tr>
<tr><td>10248</td><td>2024-07-04</td><td>1</td></tr>
<tr><td>10249</td><td>2024-07-05</td><td>2</td></tr>
<tr><td>10250</td><td>2024-07-08</td><td>3</td></tr>
<tr><td>10251</td><td>2024-07-08</td><td>4</td></tr>
<tr><td>10252</td><td>2024-07-09</td><td>5</td></tr>
<tr><td>10253</td><td>2024-07-10</td><td>6</td></tr>
</table></div>
<p class="result-more">… показано 6 з 14 рядків</p>
<!-- run:end -->

</div>

### LAG і LEAD

`LAG()` повертає значення з **попереднього** рядка, `LEAD()` — з **наступного**:

<div class="example" markdown="1">

Скільки днів минуло між замовленнями:

```sql
SELECT OrderID, OrderDate,
       LAG(OrderDate) OVER (ORDER BY OrderDate, OrderID) AS PrevDate,
       DATEDIFF(DAY,
                LAG(OrderDate) OVER (ORDER BY OrderDate, OrderID),
                OrderDate) AS DaysSincePrev
FROM Orders;
```

<!-- run:start rows=6 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>OrderDate</th><th>PrevDate</th><th>DaysSincePrev</th></tr>
<tr><td>10248</td><td>2024-07-04</td><td><span class="null">NULL</span></td><td><span class="null">NULL</span></td></tr>
<tr><td>10249</td><td>2024-07-05</td><td>2024-07-04</td><td>1</td></tr>
<tr><td>10250</td><td>2024-07-08</td><td>2024-07-05</td><td>3</td></tr>
<tr><td>10251</td><td>2024-07-08</td><td>2024-07-08</td><td>0</td></tr>
<tr><td>10252</td><td>2024-07-09</td><td>2024-07-08</td><td>1</td></tr>
<tr><td>10253</td><td>2024-07-10</td><td>2024-07-09</td><td>1</td></tr>
</table></div>
<p class="result-more">… показано 6 з 14 рядків</p>
<!-- run:end -->

</div>

Інші корисні віконні функції: `FIRST_VALUE()`, `LAST_VALUE()`, `PERCENT_RANK()`, `CUME_DIST()`.
