---
title: Коментарі
h1: Коментарі в T-SQL
---

Коментарі пояснюють частини коду або тимчасово «вимикають» інструкції. Сервер коментарі ігнорує.

## Однорядкові коментарі

Однорядковий коментар починається з `--`. Усе після `--` до кінця рядка ігнорується.

<div class="example" markdown="1">

```sql
-- Вибрати всіх клієнтів:
SELECT * FROM Customers;
```

</div>

<div class="example" markdown="1">

Коментар у кінці рядка:

```sql
SELECT * FROM Customers -- WHERE City = N'Berlin';
```

</div>

<div class="example" markdown="1">

«Вимкнути» інструкцію:

```sql
-- SELECT * FROM Customers;
SELECT * FROM Products;
```

</div>

## Багаторядкові коментарі

Багаторядковий коментар починається з `/*` і закінчується `*/`.

<div class="example" markdown="1">

```sql
/* Вибрати всі стовпці
   усіх записів
   таблиці Customers: */
SELECT * FROM Customers;
```

</div>

<div class="example" markdown="1">

«Вимкнути» кілька інструкцій:

```sql
/*
SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;
*/
SELECT * FROM Categories;
```

</div>

<div class="example" markdown="1">

Коментар усередині рядка коду:

```sql
SELECT CustomerName, /*City,*/ Country FROM Customers;
```

</div>

<div class="note" markdown="1">
На відміну від MySQL, у T-SQL символ `#` **не** є коментарем — з `#` починаються імена тимчасових таблиць. Також у SQL Server багаторядкові коментарі можна вкладати один в одного.
</div>

## Гарячі клавіші

У SSMS та VS Code виділений код можна закоментувати комбінацією **Ctrl+K, Ctrl+C**, а розкоментувати — **Ctrl+K, Ctrl+U**.
