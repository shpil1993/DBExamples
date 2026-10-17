---
title: "Реляційні СУБД (RDBMS)"
---

## Що таке RDBMS?

RDBMS (Relational Database Management System) — система керування реляційними базами даних.

RDBMS — це програма, яка дає змогу створювати, оновлювати й адмініструвати реляційну базу даних.

Більшість RDBMS використовують мову SQL для доступу до бази даних. Найпоширеніші: **Microsoft SQL Server**, **MySQL**, **PostgreSQL**, **Oracle Database**, **SQLite**.

## Що таке реляційна база даних?

Реляційна база даних зберігає дані в **таблицях**. Таблиці пов'язані (relation — «відношення», «зв'язок») між собою за допомогою спільних полів.

## Таблиці, рядки та стовпці

Таблиця складається з **стовпців** (columns, поля) і **рядків** (rows, записи).

Нижче — фрагмент таблиці `Customers` з [демо-бази](demo-db.html):

```sql
SELECT TOP (5) * FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>ContactName</th><th>Address</th><th>City</th><th>PostalCode</th><th>Country</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Obere Str. 57</td><td>Berlin</td><td>12209</td><td>Germany</td></tr>
<tr><td>2</td><td>Ana Trujillo Emparedados y helados</td><td>Ana Trujillo</td><td>Avda. de la Constitución 2222</td><td>México D.F.</td><td>05021</td><td>Mexico</td></tr>
<tr><td>3</td><td>Antonio Moreno Taquería</td><td>Antonio Moreno</td><td>Mataderos 2312</td><td>México D.F.</td><td>05023</td><td>Mexico</td></tr>
<tr><td>4</td><td>Around the Horn</td><td>Thomas Hardy</td><td>120 Hanover Sq.</td><td>London</td><td>WA1 1DP</td><td>UK</td></tr>
<tr><td>5</td><td>Berglunds snabbköp</td><td>Christina Berglund</td><td>Berguvsvägen 8</td><td>Luleå</td><td>S-958 22</td><td>Sweden</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

* **Стовпці** таблиці: `CustomerID`, `CustomerName`, `ContactName`, `Address`, `City`, `PostalCode`, `Country`. Кожен стовпець зберігає певний тип інформації про клієнта.
* **Рядок** (запис) — це окремий клієнт, тобто сукупність значень усіх стовпців.

## Зв'язки між таблицями

Подивіться на фрагмент таблиці `Orders`:

```sql
SELECT TOP (5) OrderID, CustomerID, EmployeeID, OrderDate
FROM Orders;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerID</th><th>EmployeeID</th><th>OrderDate</th></tr>
<tr><td>10248</td><td>4</td><td>5</td><td>2024-07-04</td></tr>
<tr><td>10249</td><td>1</td><td>6</td><td>2024-07-05</td></tr>
<tr><td>10250</td><td>3</td><td>4</td><td>2024-07-08</td></tr>
<tr><td>10251</td><td>7</td><td>3</td><td>2024-07-08</td></tr>
<tr><td>10252</td><td>2</td><td>4</td><td>2024-07-09</td></tr>
</table></div>
<p class="result-more">Рядків: 5</p>
<!-- run:end -->

Стовпець `CustomerID` у таблиці `Orders` посилається на стовпець `CustomerID` у таблиці `Customers`. Так ми знаємо, який клієнт зробив яке замовлення.

* `CustomerID` у таблиці `Customers` — **первинний ключ** (PRIMARY KEY): він однозначно ідентифікує кожного клієнта.
* `CustomerID` у таблиці `Orders` — **зовнішній ключ** (FOREIGN KEY): він посилається на первинний ключ іншої таблиці.

Завдяки зв'язкам дані не дублюються: ім'я й адреса клієнта зберігаються один раз у таблиці `Customers`, а в замовленні — лише номер клієнта.

## Об'єкти бази даних SQL Server

Окрім таблиць, база даних SQL Server може містити:

| Об'єкт | Опис |
|---|---|
| Таблиця (Table) | Зберігає дані у вигляді рядків і стовпців |
| Представлення (View) | Збережений запит, який поводиться як віртуальна таблиця |
| Індекс (Index) | Пришвидшує пошук даних |
| Збережена процедура (Stored Procedure) | Іменований набір інструкцій T-SQL |
| Функція (Function) | Повертає значення або таблицю |
| Тригер (Trigger) | Автоматично виконується при зміні даних |
| Схема (Schema) | Простір імен для групування об'єктів, наприклад `dbo` або `sales` |

<div class="note" markdown="1">
**Схеми.** У SQL Server повне ім'я об'єкта має вигляд `база.схема.об'єкт`, наприклад `DemoShop.dbo.Customers`. Схема за замовчуванням — `dbo`. Тому запис `Customers` і `dbo.Customers` у демо-базі означає одну й ту саму таблицю.
</div>
