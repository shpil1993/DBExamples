---
title: "Псевдоніми (Aliases)"
h1: "Псевдоніми (Aliases)"
---

Псевдоніми (aliases) використовуються, щоб дати таблиці або стовпцю **тимчасове ім'я**.

* Псевдоніми роблять імена коротшими й зрозумілішими.
* Псевдонім існує лише під час виконання запиту.
* Псевдонім створюється ключовим словом `AS` (його можна пропустити).

## Синтаксис для стовпців

```sql
SELECT column_name AS alias_name
FROM table_name;
```

## Синтаксис для таблиць

```sql
SELECT column_name(s)
FROM table_name AS alias_name;
```

## Псевдоніми стовпців

<div class="example" markdown="1">

```sql
SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ID</th><th>Customer</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td></tr>
<tr><td>2</td><td>Ana Trujillo Emparedados y helados</td></tr>
<tr><td>3</td><td>Antonio Moreno Taquería</td></tr>
</table></div>
<p class="result-more">… показано 3 з 13 рядків</p>
<!-- run:end -->

</div>

### Псевдоніми з пробілами

Якщо псевдонім містить пробіли чи спеціальні символи, візьміть його у **квадратні дужки** (або подвійні лапки):

<div class="example" markdown="1">

```sql
SELECT ProductName AS [Product Name], Price AS [Ціна, $]
FROM Products;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Product Name</th><th>Ціна, $</th></tr>
<tr><td>Chais</td><td>18.00</td></tr>
<tr><td>Chang</td><td>19.00</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td></tr>
</table></div>
<p class="result-more">… показано 3 з 15 рядків</p>
<!-- run:end -->

</div>

### Об'єднання стовпців

<div class="example" markdown="1">

Створити стовпець `FullAddress`, що об'єднує адресу, місто, індекс і країну:

```sql
SELECT CustomerName,
       CONCAT(Address, N', ', PostalCode, N' ', City, N', ', Country) AS FullAddress
FROM Customers;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>FullAddress</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Obere Str. 57, 12209 Berlin, Germany</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>Avda. de la Constitución 2222, 05021 México D.F., Mexico</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>Mataderos 2312, 05023 México D.F., Mexico</td></tr>
</table></div>
<p class="result-more">… показано 3 з 13 рядків</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
У SQL Server рядки також можна об'єднувати оператором `+`: `Address + N', ' + City`. Але якщо хоча б одне значення `NULL`, результат буде `NULL`. Функція `CONCAT()` замінює `NULL` на порожній рядок, тому вона безпечніша.
</div>

## Псевдоніми таблиць

Псевдоніми таблиць особливо зручні в запитах з кількома таблицями.

<div class="example" markdown="1">

Замовлення клієнта «Around the Horn» (з `CustomerID = 4`). Використаємо псевдоніми `c` та `o`:

```sql
SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName = N'Around the Horn'
  AND c.CustomerID = o.CustomerID;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>OrderDate</th><th>CustomerName</th></tr>
<tr><td>10248</td><td>2024-07-04</td><td>Around the Horn</td></tr>
<tr><td>10253</td><td>2024-07-10</td><td>Around the Horn</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

Без псевдонімів той самий запит виглядав би так:

```sql
SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName = N'Around the Horn'
  AND Customers.CustomerID = Orders.CustomerID;
```

Псевдоніми корисні, коли:

* у запиті бере участь кілька таблиць;
* використовуються функції;
* імена стовпців довгі або незрозумілі;
* потрібно об'єднати кілька стовпців в один.

<div class="note" markdown="1">
Псевдонім стовпця можна використовувати в `ORDER BY`, але **не** в `WHERE`, `GROUP BY` чи `HAVING` того самого запиту — вони обчислюються раніше, ніж `SELECT`.
</div>
