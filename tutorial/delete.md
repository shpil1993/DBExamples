---
title: DELETE
h1: Інструкція DELETE
---

Інструкція `DELETE` видаляє наявні записи з таблиці.

## Синтаксис

```sql
DELETE FROM table_name
WHERE condition;
```

<div class="warn" markdown="1">
**Будьте уважні при видаленні записів!** Умова `WHERE` визначає, які рядки буде видалено. Якщо пропустити `WHERE`, будуть видалені **всі** рядки таблиці.
</div>

## Приклад

<div class="example" markdown="1">

Видалити клієнта «Blauer See Delikatessen» (у нього немає замовлень):

```sql
DELETE FROM Customers
WHERE CustomerName = N'Blauer See Delikatessen';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Запит виконано. Змінено рядків: 1</p>
<!-- run:end -->

</div>

## Видалення записів, на які є посилання

Якщо на рядок посилається зовнішній ключ іншої таблиці, видалити його не вдасться. Наприклад, у клієнта `Alfreds Futterkiste` є замовлення:

```sql
DELETE FROM Customers WHERE CustomerID = 1;
```

SQL Server поверне помилку:

```text
The DELETE statement conflicted with the REFERENCE constraint "FK__Orders__Customer__...".
```

Спочатку потрібно видалити (або змінити) пов'язані замовлення. Детальніше — в уроці [FOREIGN KEY](foreign-key.html).

## Видалення всіх записів

Щоб видалити всі рядки, але залишити саму таблицю (її структуру, індекси, обмеження), використовуйте `DELETE` без `WHERE`:

```sql
DELETE FROM table_name;
```

## TRUNCATE TABLE

Для швидкого очищення великої таблиці існує інструкція `TRUNCATE TABLE`:

```sql
TRUNCATE TABLE table_name;
```

| | `DELETE` | `TRUNCATE TABLE` |
|---|---|---|
| Умова `WHERE` | Можна | Не можна — видаляє все |
| Швидкість на великих таблицях | Повільніше (логує кожен рядок) | Дуже швидко |
| Лічильник `IDENTITY` | Не скидається | Скидається до початкового значення |
| Тригери `DELETE` | Спрацьовують | Не спрацьовують |
| Таблиця, на яку посилається FOREIGN KEY | Можна (якщо немає посилань на рядки) | Не можна |

## Видалення таблиці

Щоб повністю видалити таблицю разом зі структурою, використовуйте [DROP TABLE](drop-table.html):

```sql
DROP TABLE Customers;
```
