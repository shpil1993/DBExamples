---
title: "DROP DATABASE"
h1: "Інструкція DROP DATABASE"
---

Інструкція `DROP DATABASE` видаляє існуючу базу даних.

## Синтаксис

```sql
DROP DATABASE databasename;
```

<div class="warn" markdown="1">
**Будьте обережні перед видаленням бази даних!** Видалення бази призводить до втрати всієї інформації, що в ній зберігається. Відновити її можна лише з резервної копії.
</div>

## Приклад

<div class="example" markdown="1">

Видалити базу даних `testDB`:

```sql
DROP DATABASE testDB;
```

</div>

## DROP DATABASE IF EXISTS

Починаючи з SQL Server 2016, можна використовувати `IF EXISTS`, щоб уникнути помилки, якщо бази немає:

```sql
DROP DATABASE IF EXISTS testDB;
```

## Помилка «database is currently in use»

Базу, до якої є активні підключення, видалити не можна. Також не можна видалити базу, в якій ви зараз перебуваєте. Спочатку перейдіть до іншої бази та закрийте інші підключення:

```sql
USE master;
GO
ALTER DATABASE testDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO
DROP DATABASE testDB;
```

Команда `SET SINGLE_USER WITH ROLLBACK IMMEDIATE` відключає всіх інших користувачів і відкочує їхні незавершені транзакції.
