---
title: "TRY...CATCH"
h1: "Обробка помилок: TRY...CATCH"
---

Конструкція `TRY...CATCH` дає змогу перехопити помилку під час виконання та обробити її, замість того щоб перервати весь пакет.

## Синтаксис

```sql
BEGIN TRY
    -- інструкції, які можуть спричинити помилку
END TRY
BEGIN CATCH
    -- обробка помилки
END CATCH;
```

Якщо в блоці `TRY` виникає помилка, виконання негайно переходить до блоку `CATCH`. Якщо помилок немає, блок `CATCH` пропускається.

## Приклад

<div class="example" markdown="1">

```sql
BEGIN TRY
    SELECT 1 / 0 AS Result;   -- ділення на нуль
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER()   AS ErrorNumber,
           ERROR_SEVERITY() AS Severity,
           ERROR_MESSAGE()  AS Message;
END CATCH;
```

</div>

Результат блоку `CATCH`:

| ErrorNumber | Severity | Message |
|---|---|---|
| 8134 | 16 | Divide by zero error encountered. |

## Функції інформації про помилку

Ці функції працюють лише всередині блоку `CATCH`:

| Функція | Що повертає |
|---|---|
| `ERROR_NUMBER()` | Номер помилки |
| `ERROR_MESSAGE()` | Текст повідомлення |
| `ERROR_SEVERITY()` | Рівень серйозності |
| `ERROR_STATE()` | Код стану |
| `ERROR_LINE()` | Номер рядка, де сталася помилка |
| `ERROR_PROCEDURE()` | Ім'я процедури або тригера (якщо помилка в них) |

## Приклад з порушенням обмеження

<div class="example" markdown="1">

```sql
BEGIN TRY
    INSERT INTO Orders (CustomerID, OrderDate) VALUES (999, '2024-12-31');
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNumber,
           LEFT(ERROR_MESSAGE(), 70) + N'...' AS Message;
END CATCH;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ErrorNumber</th><th>Message</th></tr>
<tr><td>547</td><td>The INSERT statement conflicted with the FOREIGN KEY constraint "FK__O...</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Генерація власної помилки: THROW

Інструкція `THROW` генерує помилку з вашим номером (від 50000) і текстом:

```sql
THROW error_number, message, state;
```

<div class="example" markdown="1">

```sql
DECLARE @Quantity INT = -5;

BEGIN TRY
    IF @Quantity <= 0
        THROW 50001, N'Кількість повинна бути більшою за нуль.', 1;

    PRINT N'Цей рядок не виконається';
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNumber, ERROR_MESSAGE() AS Message;
END CATCH;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ErrorNumber</th><th>Message</th></tr>
<tr><td>50001</td><td>Кількість повинна бути більшою за нуль.</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Повторне генерування помилки

`THROW` без параметрів усередині `CATCH` передає перехоплену помилку далі — наприклад, після відкату транзакції чи запису в журнал:

```sql
BEGIN TRY
    BEGIN TRANSACTION;
    -- ... операції ...
    COMMIT;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    -- записати помилку в журнал
    INSERT INTO ErrorLog (Number, Message, LoggedAt)
    VALUES (ERROR_NUMBER(), ERROR_MESSAGE(), SYSDATETIME());
    THROW;   -- передати помилку викликаючому коду
END CATCH;
```

## RAISERROR

У старішому коді трапляється `RAISERROR` — попередник `THROW`. Він підтримує форматування повідомлень:

```sql
RAISERROR (N'Товар %d не знайдено.', 16, 1, 42);
```

<div class="note" markdown="1">
Для нового коду Microsoft рекомендує `THROW`. Зверніть увагу: інструкція перед `THROW` повинна закінчуватися крапкою з комою `;`.
</div>

## Що TRY...CATCH не перехоплює

* помилки компіляції (синтаксичні помилки) у тому самому пакеті;
* помилки з рівнем серйозності 10 і нижче (це попередження та інформаційні повідомлення);
* помилки з рівнем 20 і вище, які розривають з'єднання.
