---
title: "Оператори"
h1: "Оператори T-SQL"
---

## Арифметичні оператори

| Оператор | Опис | Приклад |
|---|---|---|
| `+` | Додавання | `SELECT 30 + 20;` → 50 |
| `-` | Віднімання | `SELECT 30 - 20;` → 10 |
| `*` | Множення | `SELECT 30 * 20;` → 600 |
| `/` | Ділення | `SELECT 30 / 20;` → 1 (цілі числа!) |
| `%` | Остача від ділення | `SELECT 30 % 20;` → 10 |

<div class="example" markdown="1">

```sql
SELECT 30 / 20   AS IntDivision,
       30.0 / 20 AS DecimalDivision,
       30 % 20   AS Modulo;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>IntDivision</th><th>DecimalDivision</th><th>Modulo</th></tr>
<tr><td>1</td><td>1.500000</td><td>10</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="warn" markdown="1">
Ділення двох цілих чисел у SQL Server дає **ціле** число (дробова частина відкидається). Щоб отримати дробовий результат, хоча б один операнд має бути дробовим: `30.0 / 20` або `CAST(30 AS DECIMAL(10,2)) / 20`.
</div>

## Побітові оператори

| Оператор | Опис |
|---|---|
| `&` | Побітове І (AND) |
| `|` | Побітове АБО (OR) |
| `^` | Побітове виключне АБО (XOR) |
| `~` | Побітове НЕ (NOT) |

## Оператори порівняння

| Оператор | Опис |
|---|---|
| `=` | Дорівнює |
| `>` | Більше |
| `<` | Менше |
| `>=` | Більше або дорівнює |
| `<=` | Менше або дорівнює |
| `<>` | Не дорівнює |
| `!=` | Не дорівнює (нестандартний) |
| `!<` | Не менше (нестандартний) |
| `!>` | Не більше (нестандартний) |

<div class="example" markdown="1">

```sql
SELECT ProductName, Price FROM Products
WHERE Price <> 18 AND Price <= 20;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th></tr>
<tr><td>Chang</td><td>19.00</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td></tr>
<tr><td>Pavlova</td><td>17.45</td></tr>
<tr><td>Tunnbröd</td><td>9.00</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>

## Складені оператори присвоєння

Використовуються зі змінними та в `UPDATE ... SET`:

| Оператор | Опис |
|---|---|
| `+=` | Додати й присвоїти |
| `-=` | Відняти й присвоїти |
| `*=` | Помножити й присвоїти |
| `/=` | Поділити й присвоїти |
| `%=` | Остача й присвоїти |
| `&=`, `|=`, `^=` | Побітові операції з присвоєнням |

<div class="example" markdown="1">

```sql
DECLARE @counter INT = 10;
SET @counter += 5;
SET @counter *= 2;
SELECT @counter AS Result;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>Result</th></tr>
<tr><td>30</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Логічні оператори

| Оператор | Опис |
|---|---|
| `ALL` | TRUE, якщо всі значення підзапиту задовольняють умову |
| `AND` | TRUE, якщо всі умови, розділені AND, істинні |
| `ANY` / `SOME` | TRUE, якщо хоча б одне значення підзапиту задовольняє умову |
| `BETWEEN` | TRUE, якщо значення в діапазоні |
| `EXISTS` | TRUE, якщо підзапит повертає хоча б один рядок |
| `IN` | TRUE, якщо значення дорівнює одному зі списку |
| `LIKE` | TRUE, якщо значення відповідає шаблону |
| `NOT` | Заперечення умови |
| `OR` | TRUE, якщо хоча б одна з умов істинна |

## Оператор конкатенації рядків

У SQL Server оператор `+` також об'єднує рядки:

<div class="example" markdown="1">

```sql
SELECT FirstName + N' ' + LastName AS FullName
FROM Employees;
```

<!-- run:start rows=3 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>FullName</th></tr>
<tr><td>Andrew Fuller</td></tr>
<tr><td>Nancy Davolio</td></tr>
<tr><td>Janet Leverling</td></tr>
</table></div>
<p class="result-more">… показано 3 з 7 рядків</p>
<!-- run:end -->

</div>

## Пріоритет операторів

Від найвищого до найнижчого:

1. `~` (побітове НЕ)
2. `*`, `/`, `%`
3. `+` (додавання, конкатенація), `-`, `&`, `^`, `|`
4. `=`, `>`, `<`, `>=`, `<=`, `<>`, `!=`, `!>`, `!<` (порівняння)
5. `NOT`
6. `AND`
7. `ALL`, `ANY`, `BETWEEN`, `IN`, `LIKE`, `OR`, `SOME`
8. `=` (присвоєння)

Використовуйте дужки, щоб явно задати порядок обчислення.
