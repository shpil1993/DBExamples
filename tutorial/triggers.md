---
title: "Тригери"
h1: "Тригери (Triggers)"
---

**Тригер** — це особливий вид збереженої процедури, який **автоматично** виконується у відповідь на певну подію в базі даних.

У SQL Server є два основні типи тригерів:

* **DML-тригери** — спрацьовують на `INSERT`, `UPDATE`, `DELETE` у таблиці або представленні;
* **DDL-тригери** — спрацьовують на `CREATE`, `ALTER`, `DROP` та інші зміни структури.

## Синтаксис DML-тригера

```sql
CREATE TRIGGER trigger_name
ON table_name
AFTER | INSTEAD OF  INSERT, UPDATE, DELETE
AS
BEGIN
    ...
END;
```

* `AFTER` — тригер виконується **після** успішної операції (найчастіший варіант);
* `INSTEAD OF` — тригер виконується **замість** операції.

## Таблиці inserted і deleted

Усередині тригера доступні дві спеціальні віртуальні таблиці:

| Операція | `inserted` | `deleted` |
|---|---|---|
| `INSERT` | нові рядки | — |
| `DELETE` | — | видалені рядки |
| `UPDATE` | нові значення рядків | старі значення рядків |

<div class="warn" markdown="1">
Тригер у SQL Server спрацьовує **один раз на інструкцію**, а не на кожен рядок. Якщо `UPDATE` змінив 100 рядків, у таблиці `inserted` буде 100 рядків. Пишіть тригери так, щоб вони коректно обробляли кілька рядків.
</div>

## Приклад: журнал змін цін

<div class="example" markdown="1">

Створимо таблицю для журналу та тригер, який записує кожну зміну ціни:

```sql
CREATE TABLE PriceHistory (
    HistoryID INT IDENTITY PRIMARY KEY,
    ProductID INT,
    OldPrice  DECIMAL(10,2),
    NewPrice  DECIMAL(10,2),
    ChangedAt DATETIME2 DEFAULT SYSDATETIME()
);
GO

CREATE TRIGGER trg_Products_PriceChange
ON Products
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO PriceHistory (ProductID, OldPrice, NewPrice)
    SELECT d.ProductID, d.Price, i.Price
    FROM deleted AS d
    JOIN inserted AS i ON i.ProductID = d.ProductID
    WHERE d.Price <> i.Price;
END;
GO

UPDATE Products SET Price = Price + 1 WHERE CategoryID = 1;

SELECT ProductID, OldPrice, NewPrice FROM PriceHistory;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductID</th><th>OldPrice</th><th>NewPrice</th></tr>
<tr><td>2</td><td>19.00</td><td>20.00</td></tr>
<tr><td>1</td><td>18.00</td><td>19.00</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Приклад: заборона операції

<div class="example" markdown="1">

Не дозволяти видаляти категорії, у яких є товари:

```sql
CREATE TRIGGER trg_Categories_NoDelete
ON Categories
INSTEAD OF DELETE
AS
BEGIN
    SET NOCOUNT ON;
    IF EXISTS (SELECT 1 FROM deleted d JOIN Products p ON p.CategoryID = d.CategoryID)
    BEGIN
        THROW 50001, N'Неможливо видалити категорію, у якій є товари.', 1;
    END;

    DELETE FROM Categories
    WHERE CategoryID IN (SELECT CategoryID FROM deleted);
END;
```

</div>

## Функції UPDATE() та COLUMNS_UPDATED()

У тригері `UPDATE` можна перевірити, чи змінювався конкретний стовпець:

```sql
IF UPDATE(Price)
BEGIN
    PRINT N'Ціну було змінено';
END
```

## DDL-тригер

<div class="example" markdown="1">

Заборонити видалення таблиць у базі даних:

```sql
CREATE TRIGGER trg_NoDropTable
ON DATABASE
FOR DROP_TABLE
AS
BEGIN
    PRINT N'Видалення таблиць заборонено!';
    ROLLBACK;
END;
```

</div>

## Керування тригерами

```sql
-- Вимкнути / увімкнути тригер
DISABLE TRIGGER trg_Products_PriceChange ON Products;
ENABLE  TRIGGER trg_Products_PriceChange ON Products;

-- Видалити тригер
DROP TRIGGER IF EXISTS trg_Products_PriceChange;

-- DDL-тригер рівня бази даних
DROP TRIGGER IF EXISTS trg_NoDropTable ON DATABASE;

-- Перелік тригерів
SELECT name, parent_class_desc, is_disabled FROM sys.triggers;
```

<div class="note" markdown="1">
Тригери — потужний, але «невидимий» інструмент: їхні дії не очевидні з коду застосунку. Використовуйте їх помірно — для аудиту, перевірки складних правил цілісності тощо.
</div>
