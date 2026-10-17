---
title: LIKE
h1: Оператор LIKE
---

Оператор `LIKE` використовується в умові `WHERE` для пошуку значень за **шаблоном**.

У шаблонах найчастіше використовують два символи:

* `%` — будь-яка кількість символів (нуль, один або більше);
* `_` — рівно один будь-який символ.

SQL Server також підтримує шаблони `[ ]` та `[^ ]` — див. урок [Символи-шаблони](wildcards.html).

## Синтаксис

```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

## Символ %

<div class="example" markdown="1">

Клієнти, назва яких починається на «a»:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'a%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Alfreds Futterkiste</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td></tr>
<tr><td>Antonio Moreno Taquería</td></tr>
<tr><td>Around the Horn</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Клієнти, назва яких закінчується на «a»:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'%a';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Antonio Moreno Taquería</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Клієнти, назва яких містить «or» у будь-якому місці:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'%or%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Antonio Moreno Taquería</td></tr>
<tr><td>Around the Horn</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Символ _

<div class="example" markdown="1">

Клієнти з міст, назва яких починається на «L» і складається рівно з 4 символів:

```sql
SELECT CustomerName, City FROM Customers
WHERE City LIKE N'L___';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th></tr>
<tr><td>Lviv Coffee House</td><td>Lviv</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Назва, де «r» стоїть на другій позиції:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'_r%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Around the Horn</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Комбінації

| Шаблон | Значення |
|---|---|
| `LIKE 'a%'` | Починається на «a» |
| `LIKE '%a'` | Закінчується на «a» |
| `LIKE '%or%'` | Містить «or» |
| `LIKE '_r%'` | «r» на другій позиції |
| `LIKE 'a_%'` | Починається на «a» і має щонайменше 2 символи |
| `LIKE 'a%o'` | Починається на «a» і закінчується на «o» |

<div class="example" markdown="1">

Назва починається на «a» і має щонайменше 3 символи:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'a__%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Alfreds Futterkiste</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td></tr>
<tr><td>Antonio Moreno Taquería</td></tr>
<tr><td>Around the Horn</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>

## NOT LIKE

<div class="example" markdown="1">

Товари, назва яких не починається на «C»:

```sql
SELECT ProductName FROM Products
WHERE ProductName NOT LIKE N'C%';
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductName</th></tr>
<tr><td>Aniseed Syrup</td></tr>
<tr><td>Grandma's Boysenberry Spread</td></tr>
<tr><td>Uncle Bob's Organic Dried Pears</td></tr>
<tr><td>Northwoods Cranberry Sauce</td></tr>
<tr><td>Mishi Kobe Niku</td></tr>
</table></div>
<p class="result-more">… показано 5 з 11 рядків</p>
<!-- run:end -->

</div>

## Без символів-шаблонів

Якщо шаблон не містить `%` чи `_`, `LIKE` працює як звичайне порівняння `=`:

```sql
SELECT * FROM Customers
WHERE Country LIKE N'Spain';
```

<div class="note" markdown="1">
Чи розрізняє `LIKE` великі й малі літери, залежить від collation стовпця. За замовчуванням (`..._CI_AS`) — **не розрізняє**, тому `'a%'` знаходить і «Alfreds», і «around».
</div>
