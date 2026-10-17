---
title: "Транзакції"
h1: "Транзакції"
---

**Транзакція** — це група операцій, яка виконується як **одне ціле**: або всі зміни зберігаються, або жодна.

Класичний приклад — переказ грошей: списання з одного рахунку та зарахування на інший повинні відбутися разом. Якщо після списання станеться збій, гроші не повинні «зникнути».

## Властивості ACID

| Властивість | Опис |
|---|---|
| **A**tomicity (атомарність) | Усі операції транзакції виконуються повністю або не виконуються зовсім |
| **C**onsistency (узгодженість) | Транзакція переводить базу з одного коректного стану в інший |
| **I**solation (ізольованість) | Паралельні транзакції не бачать проміжних змін одна одної |
| **D**urability (довговічність) | Підтверджені зміни зберігаються навіть після збою сервера |

## Команди керування транзакціями

| Команда | Опис |
|---|---|
| `BEGIN TRANSACTION` (або `BEGIN TRAN`) | Почати транзакцію |
| `COMMIT` (або `COMMIT TRANSACTION`) | Підтвердити (зберегти) зміни |
| `ROLLBACK` (або `ROLLBACK TRANSACTION`) | Скасувати всі зміни транзакції |
| `SAVE TRANSACTION name` | Створити точку збереження |

## Приклад COMMIT

<div class="example" markdown="1">

```sql
BEGIN TRANSACTION;

UPDATE Products SET Price = Price - 1 WHERE ProductID = 1;
UPDATE Products SET Price = Price + 1 WHERE ProductID = 2;

COMMIT;
```

</div>

## Приклад ROLLBACK

<div class="example" markdown="1">

```sql
BEGIN TRANSACTION;

DELETE FROM OrderDetails WHERE OrderID = 10248;
SELECT COUNT(*) AS RowsInsideTran FROM OrderDetails WHERE OrderID = 10248;

ROLLBACK;

SELECT COUNT(*) AS RowsAfterRollback FROM OrderDetails WHERE OrderID = 10248;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>RowsInsideTran</th></tr>
<tr><td>0</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<div class="table-scroll"><table>
<tr><th>RowsAfterRollback</th></tr>
<tr><td>3</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

Після `ROLLBACK` видалені рядки повернулися.

## Автоматичні транзакції

За замовчуванням SQL Server працює в режимі **autocommit**: кожна окрема інструкція (`INSERT`, `UPDATE`, `DELETE`) — це окрема транзакція, яка автоматично підтверджується після успішного виконання. Явний `BEGIN TRANSACTION` потрібен, щоб об'єднати кілька інструкцій.

## Транзакція з обробкою помилок

Правильний шаблон — поєднання транзакції з `TRY...CATCH`:

<div class="example" markdown="1">

Переказ коштів між рахунками:

```sql
CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY,
    Owner     NVARCHAR(50),
    Balance   DECIMAL(10,2) CHECK (Balance >= 0)
);
INSERT INTO Accounts VALUES (1, N'Олена', 500), (2, N'Тарас', 100);
GO

BEGIN TRY
    BEGIN TRANSACTION;

    UPDATE Accounts SET Balance = Balance - 700 WHERE AccountID = 1;  -- порушить CHECK
    UPDATE Accounts SET Balance = Balance + 700 WHERE AccountID = 2;

    COMMIT;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    PRINT N'Переказ скасовано: ' + ERROR_MESSAGE();
END CATCH;

SELECT * FROM Accounts;
```

<div class="result-label">Повідомлення:</div>

```text
Переказ скасовано: The UPDATE statement conflicted with the CHECK constraint "CK__Accounts__Balanc__...".
```

<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>AccountID</th><th>Owner</th><th>Balance</th></tr>
<tr><td>1</td><td>Олена</td><td>500.00</td></tr>
<tr><td>2</td><td>Тарас</td><td>100.00</td></tr>
</table></div>

</div>

Перше оновлення порушило обмеження `CHECK`, виконання перейшло до блоку `CATCH`, і транзакцію було відкочено — баланси не змінилися.

<div class="note" markdown="1">
Інструкція `SET XACT_ABORT ON` на початку пакета або процедури змушує SQL Server автоматично відкочувати всю транзакцію при будь-якій помилці. Її рекомендують вмикати в процедурах, що використовують транзакції.
</div>

## Точки збереження

`SAVE TRANSACTION` дає змогу відкотити лише частину транзакції:

```sql
BEGIN TRANSACTION;

INSERT INTO Shippers (ShipperName) VALUES (N'Shipper A');
SAVE TRANSACTION AfterA;

INSERT INTO Shippers (ShipperName) VALUES (N'Shipper B');
ROLLBACK TRANSACTION AfterA;   -- скасувати лише вставку Shipper B

COMMIT;                        -- зберегти Shipper A
```

## Рівні ізоляції

Рівень ізоляції визначає, наскільки транзакції «бачать» зміни одна одної:

| Рівень | Опис |
|---|---|
| `READ UNCOMMITTED` | Можна читати непідтверджені зміни («брудне читання») |
| `READ COMMITTED` | **За замовчуванням.** Читаються лише підтверджені дані |
| `REPEATABLE READ` | Прочитані рядки не можуть бути змінені іншими до кінця транзакції |
| `SNAPSHOT` | Транзакція бачить знімок даних на момент свого початку |
| `SERIALIZABLE` | Найсуворіший: транзакції виконуються так, ніби послідовно |

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```
