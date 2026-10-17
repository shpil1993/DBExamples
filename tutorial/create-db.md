---
title: "CREATE DATABASE"
h1: "Інструкція CREATE DATABASE"
---

Інструкція `CREATE DATABASE` створює нову базу даних.

## Синтаксис

```sql
CREATE DATABASE databasename;
```

## Приклад

<div class="example" markdown="1">

Створити базу даних `testDB`:

```sql
CREATE DATABASE testDB;
```

</div>

<div class="note" markdown="1">
Для створення бази даних потрібні права адміністратора (наприклад, роль `sysadmin` або `dbcreator`).
</div>

Після створення базу можна побачити в переліку баз даних:

```sql
SELECT name, database_id, create_date
FROM sys.databases;
```

## Перехід до бази даних: USE

Щоб наступні запити виконувалися в новій базі, перемкніться на неї командою `USE`:

```sql
USE testDB;
```

## Створення з параметрами файлів

Кожна база даних SQL Server складається щонайменше з двох файлів:

* **файл даних** (`.mdf`) — зберігає таблиці, індекси та інші об'єкти;
* **файл журналу транзакцій** (`.ldf`) — зберігає історію змін для відновлення.

За замовчуванням SQL Server сам обирає розташування і розмір файлів. Їх можна задати явно:

```sql
CREATE DATABASE SalesDB
ON PRIMARY (
    NAME = SalesDB_data,
    FILENAME = 'C:\SQLData\SalesDB.mdf',
    SIZE = 100MB,
    FILEGROWTH = 50MB
)
LOG ON (
    NAME = SalesDB_log,
    FILENAME = 'C:\SQLData\SalesDB_log.ldf',
    SIZE = 50MB,
    FILEGROWTH = 25MB
);
```

## Створення, якщо бази ще немає

```sql
IF DB_ID(N'testDB') IS NULL
    CREATE DATABASE testDB;
```

Функція `DB_ID()` повертає ідентифікатор бази або `NULL`, якщо такої бази немає.

## Collation (правила порівняння)

Collation визначає, як порівнюються та сортуються рядки (чутливість до регістру, акцентів, мова). Його можна вказати під час створення бази:

```sql
CREATE DATABASE UkrainianDB
COLLATE Ukrainian_CI_AS;
```

* `CI` — Case Insensitive (регістр не враховується), `CS` — Case Sensitive;
* `AS` — Accent Sensitive (наголоси/діакритика враховуються), `AI` — Accent Insensitive.
