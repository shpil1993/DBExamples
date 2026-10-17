---
title: "SELECT"
h1: "Інструкція SELECT"
---

Інструкція `SELECT` використовується для вибору (читання) даних з бази даних.

Дані, які повертає запит, називаються **результуючим набором** (result set).

## Синтаксис SELECT

```sql
SELECT column1, column2, ...
FROM table_name;
```

Тут `column1, column2, ...` — імена стовпців таблиці, які потрібно отримати, а `table_name` — ім'я таблиці.

Щоб вибрати **всі** стовпці таблиці, використовуйте зірочку `*`:

```sql
SELECT * FROM table_name;
```

## Приклад: вибір окремих стовпців

<div class="example" markdown="1">

Вибрати стовпці `CustomerName`, `City` і `Country` з таблиці `Customers`:

```sql
SELECT CustomerName, City, Country
FROM Customers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th><th>Country</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Berlin</td><td>Germany</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td><td>México D.F.</td><td>Mexico</td></tr>
<tr><td>Antonio Moreno Taquería</td><td>México D.F.</td><td>Mexico</td></tr>
<tr><td>Around the Horn</td><td>London</td><td>UK</td></tr>
<tr><td>Berglunds snabbköp</td><td>Luleå</td><td>Sweden</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Mannheim</td><td>Germany</td></tr>
<tr><td>Blondel père et fils</td><td>Strasbourg</td><td>France</td></tr>
<tr><td>Bólido Comidas preparadas</td><td>Madrid</td><td>Spain</td></tr>
<tr><td>Bon app'</td><td>Marseille</td><td>France</td></tr>
<tr><td>Bottom-Dollar Marketse</td><td>Tsawassen</td><td>Canada</td></tr>
</table></div>
<p class="result-more">… показано 10 з 13 рядків</p>
<!-- run:end -->

</div>

## Приклад: вибір усіх стовпців

<div class="example" markdown="1">

Вибрати всі стовпці таблиці `Shippers`:

```sql
SELECT * FROM Shippers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ShipperID</th><th>ShipperName</th><th>Phone</th></tr>
<tr><td>1</td><td>Speedy Express</td><td>(503) 555-9831</td></tr>
<tr><td>2</td><td>United Package</td><td>(503) 555-3199</td></tr>
<tr><td>3</td><td>Federal Shipping</td><td>(503) 555-9931</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
**Порада.** У реальних застосунках краще явно перелічувати потрібні стовпці замість `SELECT *`. Так запит передає менше даних, а код не «ламається», якщо до таблиці додадуть новий стовпець.
</div>

## Обчислювані стовпці

У списку `SELECT` можна не лише перелічувати стовпці, а й обчислювати вирази:

<div class="example" markdown="1">

Показати ціну товару і ціну з ПДВ 20%:

```sql
SELECT ProductName, Price, Price * 1.2 AS PriceWithVAT
FROM Products;
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th><th>Price</th><th>PriceWithVAT</th></tr>
<tr><td>Chais</td><td>18.00</td><td>21.600</td></tr>
<tr><td>Chang</td><td>19.00</td><td>22.800</td></tr>
<tr><td>Aniseed Syrup</td><td>10.00</td><td>12.000</td></tr>
<tr><td>Chef Anton's Cajun Seasoning</td><td>22.00</td><td>26.400</td></tr>
<tr><td>Chef Anton's Gumbo Mix</td><td>21.35</td><td>25.620</td></tr>
</table></div>
<p class="result-more">… показано 5 з 15 рядків</p>
<!-- run:end -->

</div>

Ключове слово `AS` задає ім'я (псевдонім) для обчислюваного стовпця. Детальніше — в уроці [Псевдоніми](aliases.html).

## SELECT без таблиці

У SQL Server `SELECT` можна використовувати навіть без `FROM` — наприклад, щоб обчислити вираз або викликати функцію:

<div class="example" markdown="1">

```sql
SELECT 2 + 3 AS Sum, GETDATE() AS CurrentDate, N'Привіт, SQL Server!' AS Greeting;
```

</div>

## Регістр і крапка з комою

* Ключові слова SQL **не чутливі до регістру**: `select` і `SELECT` — те саме. Прийнято писати їх великими літерами.
* Чутливість до регістру **даних** (наприклад, `'germany'` і `'Germany'`) залежить від налаштування *collation* (правил порівняння). За замовчуванням SQL Server регістр не розрізняє.
* Крапка з комою `;` у кінці інструкції в T-SQL здебільшого необов'язкова, але Microsoft рекомендує її ставити — у деяких конструкціях (наприклад, перед `WITH` для CTE) вона обов'язкова.

## Рядки Unicode: префікс N

Рядкові літерали з префіксом `N` (наприклад, `N'Київ'`) мають тип Unicode (`NVARCHAR`). Використовуйте префікс `N` завжди, коли рядок може містити кирилицю чи інші не-латинські символи — інакше вони можуть перетворитися на знаки питання.

```sql
SELECT N'Україна' AS WithN, 'Україна' AS WithoutN;
```
