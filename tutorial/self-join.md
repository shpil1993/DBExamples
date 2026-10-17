---
title: Self Join
h1: Self Join (самоз'єднання)
---

**Self join** — це звичайне з'єднання, у якому таблиця з'єднується **сама з собою**.

Щоб розрізняти дві «копії» таблиці, обов'язково використовуються різні псевдоніми.

## Синтаксис

```sql
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```

або з явним `JOIN`:

```sql
SELECT column_name(s)
FROM table1 AS T1
JOIN table1 AS T2 ON condition;
```

## Приклад: працівники та їхні керівники

У таблиці `Employees` стовпець `ManagerID` посилається на `EmployeeID` цієї ж таблиці. Виведемо кожного працівника разом з ім'ям керівника:

<div class="example" markdown="1">

```sql
SELECT e.FirstName + N' ' + e.LastName AS Employee,
       m.FirstName + N' ' + m.LastName AS Manager
FROM Employees AS e
LEFT JOIN Employees AS m ON e.ManagerID = m.EmployeeID;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Employee</th><th>Manager</th></tr>
<tr><td>Andrew Fuller</td><td><span class="null">NULL</span></td></tr>
<tr><td>Nancy Davolio</td><td>Andrew Fuller</td></tr>
<tr><td>Janet Leverling</td><td>Andrew Fuller</td></tr>
<tr><td>Margaret Peacock</td><td>Andrew Fuller</td></tr>
<tr><td>Steven Buchanan</td><td>Andrew Fuller</td></tr>
<tr><td>Michael Suyama</td><td>Steven Buchanan</td></tr>
<tr><td>Robert King</td><td>Steven Buchanan</td></tr>
</table></div>
<p class="result-more">Рядків: 7</p>
<!-- run:end -->

</div>

Ми використали `LEFT JOIN`, щоб у результат потрапив і керівник верхнього рівня (*Andrew Fuller*), у якого немає свого керівника.

## Приклад: клієнти з одного міста

<div class="example" markdown="1">

Знайти пари клієнтів з одного міста:

```sql
SELECT A.CustomerName AS CustomerName1,
       B.CustomerName AS CustomerName2,
       A.City
FROM Customers AS A, Customers AS B
WHERE A.CustomerID < B.CustomerID
  AND A.City = B.City
ORDER BY A.City;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName1</th><th>CustomerName2</th><th>City</th></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>Antonio Moreno Taquería</td><td>México D.F.</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Умова `A.CustomerID < B.CustomerID` прибирає пари клієнта з самим собою та дублікати (A–B і B–A).
