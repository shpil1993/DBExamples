---
title: Символи-шаблони
h1: Символи-шаблони (Wildcards)
---

Символ-шаблон (wildcard) замінює один або кілька символів у рядку. Шаблони використовуються з оператором [LIKE](like.html).

## Символи-шаблони в SQL Server

| Символ | Опис | Приклад |
|---|---|---|
| `%` | Нуль або більше будь-яких символів | `bl%` знайде bl, black, blue, blob |
| `_` | Один будь-який символ | `h_t` знайде hot, hat, hit |
| `[]` | Будь-який один символ із перелічених у дужках | `h[oa]t` знайде hot і hat, але не hit |
| `[^]` | Будь-який один символ, **крім** перелічених | `h[^oa]t` знайде hit, але не hot і hat |
| `-` | Діапазон символів (усередині `[]`) | `c[a-b]t` знайде cat і cbt |

<div class="note" markdown="1">
Шаблони `[]` та `[^]` — особливість SQL Server (у MySQL їх немає; там для цього використовують `REGEXP`).
</div>

## Символ %

<div class="example" markdown="1">

Клієнти з міст, що починаються на «Ber»:

```sql
SELECT CustomerName, City FROM Customers
WHERE City LIKE N'ber%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Berlin</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

<div class="example" markdown="1">

Клієнти з міст, що містять «es»:

```sql
SELECT CustomerName, City FROM Customers
WHERE City LIKE N'%es%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th></tr>
<tr><td>Odesa Seafood</td><td>Odesa</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Символ _

<div class="example" markdown="1">

Місто з будь-яким першим символом, а далі «ondon»:

```sql
SELECT CustomerName, City FROM Customers
WHERE City LIKE N'_ondon';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th></tr>
<tr><td>Around the Horn</td><td>London</td></tr>
</table></div>
<p class="result-more">Рядків: 1</p>
<!-- run:end -->

</div>

## Символ []

<div class="example" markdown="1">

Клієнти, назва яких починається на «b», «s» або «p»:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'[bsp]%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Berglunds snabbköp</td></tr>
<tr><td>Blauer See Delikatessen</td></tr>
<tr><td>Blondel père et fils</td></tr>
<tr><td>Bólido Comidas preparadas</td></tr>
<tr><td>Bon app'</td></tr>
<tr><td>Bottom-Dollar Marketse</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

</div>

## Символ - (діапазон)

<div class="example" markdown="1">

Клієнти, назва яких починається на літеру від «a» до «c»:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'[a-c]%';
```

<!-- run:start rows=5 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Alfreds Futterkiste</td></tr>
<tr><td>Ana Trujillo Emparedados y helados</td></tr>
<tr><td>Antonio Moreno Taquería</td></tr>
<tr><td>Around the Horn</td></tr>
<tr><td>Berglunds snabbköp</td></tr>
</table></div>
<p class="result-more">… показано 5 з 10 рядків</p>
<!-- run:end -->

</div>

## Символ [^]

<div class="example" markdown="1">

Клієнти, назва яких **не** починається на «a», «b» або «c»:

```sql
SELECT CustomerName FROM Customers
WHERE CustomerName LIKE N'[^a-c]%';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th></tr>
<tr><td>Kyiv Market</td></tr>
<tr><td>Lviv Coffee House</td></tr>
<tr><td>Odesa Seafood</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

</div>

## Пошук самих символів %, _ або [

Щоб знайти символ, який є шаблоном, візьміть його в квадратні дужки або використайте `ESCAPE`:

```sql
-- Знайти рядки, що містять символ %
SELECT * FROM Products WHERE ProductName LIKE N'%[%]%';

-- Те саме з ESCAPE: символ ! "екранує" наступний символ
SELECT * FROM Products WHERE ProductName LIKE N'%!%%' ESCAPE '!';
```
