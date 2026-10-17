---
title: "DROP TABLE"
h1: "Інструкція DROP TABLE"
---

Інструкція `DROP TABLE` видаляє існуючу таблицю разом з усіма даними, індексами, тригерами та обмеженнями.

## Синтаксис

```sql
DROP TABLE table_name;
```

<div class="warn" markdown="1">
**Будьте обережні!** Видалення таблиці призводить до втрати всієї інформації в ній.
</div>

## Приклад

<div class="example" markdown="1">

Видалити таблицю `OrderDetails`:

```sql
DROP TABLE OrderDetails;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## DROP TABLE IF EXISTS

Починаючи з SQL Server 2016:

```sql
DROP TABLE IF EXISTS dbo.Persons;
```

Якщо таблиці немає, інструкція просто нічого не зробить, а не поверне помилку.

## Таблиці, на які посилаються зовнішні ключі

Якщо на таблицю посилається `FOREIGN KEY` іншої таблиці, видалити її не можна:

```sql
DROP TABLE Customers;
```

```text
Could not drop object 'Customers' because it is referenced by a FOREIGN KEY constraint.
```

Спочатку потрібно видалити залежну таблицю або обмеження зовнішнього ключа.

## Видалення кількох таблиць

```sql
DROP TABLE IF EXISTS dbo.Table1, dbo.Table2, dbo.Table3;
```

## TRUNCATE TABLE

Щоб видалити лише **дані**, але залишити саму таблицю, використовуйте `TRUNCATE TABLE`:

```sql
TRUNCATE TABLE table_name;
```

Порівняння `TRUNCATE` і `DELETE` — в уроці [DELETE](delete.html).
