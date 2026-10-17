---
title: "Функції дати й часу"
h1: "Функції дати й часу SQL Server"
---

Функції для отримання поточної дати, виділення частин дати, арифметики дат і форматування. Детальніше про роботу з датами — в уроці [Робота з датами](dates.html).

Колонка «Результат» отримана виконанням прикладу на SQL Server 2022 з демо-базою DemoShop.

<div class="table-scroll"><table>
<tr><th>Функція</th><th>Опис</th><th>Приклад</th><th>Результат</th></tr>
<tr><td><strong>CURRENT_TIMESTAMP</strong></td><td>Поточна дата й час (стандарт SQL, аналог GETDATE)</td><td><code>SELECT CURRENT_TIMESTAMP;</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>DATEADD</strong></td><td>Додає інтервал до дати</td><td><code>SELECT DATEADD(MONTH, 2, '2024-07-08');</code></td><td>2024-09-08 00:00:00.000</td></tr>
<tr><td><strong>DATEDIFF</strong></td><td>Повертає різницю між двома датами у вказаних одиницях</td><td><code>SELECT DATEDIFF(DAY, '2024-07-08', '2024-12-31');</code></td><td>176</td></tr>
<tr><td><strong>DATEDIFF_BIG</strong></td><td>Як DATEDIFF, але повертає BIGINT</td><td><code>SELECT DATEDIFF_BIG(SECOND, '2000-01-01', '2024-01-01');</code></td><td>757382400</td></tr>
<tr><td><strong>DATEFROMPARTS</strong></td><td>Створює дату з року, місяця й дня</td><td><code>SELECT DATEFROMPARTS(2024, 8, 24);</code></td><td>2024-08-24</td></tr>
<tr><td><strong>DATENAME</strong></td><td>Повертає назву частини дати як рядок</td><td><code>SELECT DATENAME(MONTH, '2024-07-08');</code></td><td>July</td></tr>
<tr><td><strong>DATEPART</strong></td><td>Повертає частину дати як ціле число</td><td><code>SELECT DATEPART(QUARTER, '2024-07-08');</code></td><td>3</td></tr>
<tr><td><strong>DATETRUNC</strong></td><td>Обрізає дату до вказаної частини (2022+)</td><td><code>SELECT DATETRUNC(MONTH, CAST('2024-07-08' AS DATE));</code></td><td>2024-07-01</td></tr>
<tr><td><strong>DATETIMEFROMPARTS</strong></td><td>Створює DATETIME з частин</td><td><code>SELECT DATETIMEFROMPARTS(2024, 7, 8, 14, 30, 0, 0);</code></td><td>2024-07-08 14:30:00.000</td></tr>
<tr><td><strong>DAY</strong></td><td>Повертає день місяця</td><td><code>SELECT DAY('2024-07-08');</code></td><td>8</td></tr>
<tr><td><strong>EOMONTH</strong></td><td>Повертає останній день місяця</td><td><code>SELECT EOMONTH('2024-02-10');</code></td><td>2024-02-29</td></tr>
<tr><td><strong>GETDATE</strong></td><td>Поточна дата й час сервера (DATETIME)</td><td><code>SELECT GETDATE();</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>GETUTCDATE</strong></td><td>Поточна дата й час UTC (DATETIME)</td><td><code>SELECT GETUTCDATE();</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>ISDATE</strong></td><td>Перевіряє, чи є рядок коректною датою (1 або 0)</td><td><code>SELECT ISDATE('2024-02-30');</code></td><td>0</td></tr>
<tr><td><strong>MONTH</strong></td><td>Повертає місяць</td><td><code>SELECT MONTH('2024-07-08');</code></td><td>7</td></tr>
<tr><td><strong>SYSDATETIME</strong></td><td>Поточна дата й час з високою точністю (DATETIME2)</td><td><code>SELECT SYSDATETIME();</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>SYSDATETIMEOFFSET</strong></td><td>Поточна дата й час з часовим поясом</td><td><code>SELECT SYSDATETIMEOFFSET();</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>SYSUTCDATETIME</strong></td><td>Поточна дата й час UTC (DATETIME2)</td><td><code>SELECT SYSUTCDATETIME();</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>SWITCHOFFSET</strong></td><td>Змінює часовий пояс значення DATETIMEOFFSET</td><td><code>SELECT SWITCHOFFSET(CAST('2024-07-08 12:00 +00:00' AS DATETIMEOFFSET), '+03:00');</code></td><td>2024-07-08 15:00:00.000+03:00</td></tr>
<tr><td><strong>TODATETIMEOFFSET</strong></td><td>Додає часовий пояс до DATETIME2</td><td><code>SELECT TODATETIMEOFFSET(CAST('2024-07-08 12:00' AS DATETIME2(0)), '+02:00');</code></td><td>2024-07-08 12:00:00.000+02:00</td></tr>
<tr><td><strong>YEAR</strong></td><td>Повертає рік</td><td><code>SELECT YEAR('2024-07-08');</code></td><td>2024</td></tr>
</table></div>

## Частини дати (datepart)

Функції `DATEADD`, `DATEDIFF`, `DATENAME`, `DATEPART` і `DATETRUNC` приймають такі назви частин дати:

| Частина | Скорочення |
|---|---|
| `YEAR` | `yy`, `yyyy` |
| `QUARTER` | `qq`, `q` |
| `MONTH` | `mm`, `m` |
| `DAYOFYEAR` | `dy`, `y` |
| `DAY` | `dd`, `d` |
| `WEEK` | `wk`, `ww` |
| `WEEKDAY` | `dw` |
| `HOUR` | `hh` |
| `MINUTE` | `mi`, `n` |
| `SECOND` | `ss`, `s` |
| `MILLISECOND` | `ms` |
| `MICROSECOND` | `mcs` |
| `NANOSECOND` | `ns` |

## Стилі CONVERT для дат

| Стиль | Формат | Приклад |
|---|---|---|
| 23 | `yyyy-mm-dd` | `CONVERT(VARCHAR, @d, 23)` → 2024-07-08 |
| 104 | `dd.mm.yyyy` | `CONVERT(VARCHAR, @d, 104)` → 08.07.2024 |
| 103 | `dd/mm/yyyy` | `CONVERT(VARCHAR, @d, 103)` → 08/07/2024 |
| 101 | `mm/dd/yyyy` | `CONVERT(VARCHAR, @d, 101)` → 07/08/2024 |
| 112 | `yyyymmdd` | `CONVERT(VARCHAR, @d, 112)` → 20240708 |
| 120 | `yyyy-mm-dd hh:mi:ss` | `CONVERT(VARCHAR, @dt, 120)` → 2024-07-08 14:30:00 |

