---
title: "CREATE INDEX"
h1: "Інструкція CREATE INDEX"
---

Інструкція `CREATE INDEX` створює **індекс** у таблиці.

Індекси дають змогу знаходити дані значно швидше. Користувачі індекси не бачать — вони лише пришвидшують пошук і запити.

<div class="note" markdown="1">
Оновлення таблиці з індексами займає більше часу, ніж таблиці без них, бо індекси теж треба оновлювати. Тому створюйте індекси лише на стовпцях, за якими часто виконується пошук, з'єднання чи сортування.
</div>

## Синтаксис

Створює індекс; повторювані значення дозволені:

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

Створює **унікальний** індекс; повторювані значення заборонені:

```sql
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);
```

## Приклад

<div class="example" markdown="1">

Індекс за прізвищем працівників:

```sql
CREATE INDEX IX_Employees_LastName
ON Employees (LastName);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Індекс з кількох стовпців:

```sql
CREATE INDEX IX_Employees_Name
ON Employees (LastName, FirstName);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## Кластерні та некластерні індекси

У SQL Server є два основні типи індексів:

| | Кластерний (`CLUSTERED`) | Некластерний (`NONCLUSTERED`) |
|---|---|---|
| Що це | Дані таблиці фізично впорядковані за ключем індексу | Окрема структура з посиланнями на рядки |
| Скільки на таблицю | Лише **один** | Багато (до 999) |
| За замовчуванням | Створюється для `PRIMARY KEY` | Створюється `CREATE INDEX` |

```sql
CREATE CLUSTERED INDEX IX_Log_Date ON EventLog (EventDate);
CREATE NONCLUSTERED INDEX IX_Log_Type ON EventLog (EventType);
```

## Включені стовпці (INCLUDE)

Некластерний індекс може «нести» додаткові стовпці. Тоді запит може отримати всі потрібні дані прямо з індексу, не звертаючись до таблиці:

<div class="example" markdown="1">

```sql
CREATE INDEX IX_Products_Category
ON Products (CategoryID)
INCLUDE (ProductName, Price);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## Фільтрований індекс

Індекс лише для частини рядків:

```sql
CREATE INDEX IX_Orders_NoEmployee
ON Orders (OrderDate)
WHERE EmployeeID IS NULL;
```

## Перегляд індексів таблиці

<div class="example" markdown="1">

```sql
SELECT i.name AS IndexName, i.type_desc, i.is_unique, i.is_primary_key
FROM sys.indexes AS i
WHERE i.object_id = OBJECT_ID(N'dbo.Products') AND i.name IS NOT NULL;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>IndexName</th><th>type_desc</th><th>is_unique</th><th>is_primary_key</th></tr>
<tr><td>PK__Products__B40CC6EDD880B984</td><td>CLUSTERED</td><td>1</td><td>1</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## DROP INDEX

Видалити індекс:

```sql
DROP INDEX IX_Employees_LastName ON Employees;

-- або з перевіркою існування
DROP INDEX IF EXISTS IX_Employees_LastName ON Employees;
```
