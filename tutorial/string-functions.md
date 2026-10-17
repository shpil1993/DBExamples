---
title: "Рядкові функції"
h1: "Рядкові функції SQL Server"
---

Функції для роботи з текстом: пошук, заміна, вирізання частин рядка, зміна регістру тощо.

Колонка «Результат» отримана виконанням прикладу на SQL Server 2022 з демо-базою DemoShop.

<div class="table-scroll"><table>
<tr><th>Функція</th><th>Опис</th><th>Приклад</th><th>Результат</th></tr>
<tr><td><strong>ASCII</strong></td><td>Повертає ASCII-код першого символу рядка</td><td><code>SELECT ASCII('A');</code></td><td>65</td></tr>
<tr><td><strong>CHAR</strong></td><td>Повертає символ за ASCII-кодом</td><td><code>SELECT CHAR(65);</code></td><td>A</td></tr>
<tr><td><strong>CHARINDEX</strong></td><td>Повертає позицію підрядка в рядку (0, якщо не знайдено)</td><td><code>SELECT CHARINDEX('t', 'Customer');</code></td><td>4</td></tr>
<tr><td><strong>CONCAT</strong></td><td>Об'єднує два або більше рядків (NULL замінюється на порожній рядок)</td><td><code>SELECT CONCAT('SQL', ' ', 'Server');</code></td><td>SQL Server</td></tr>
<tr><td><strong>CONCAT_WS</strong></td><td>Об'єднує рядки через роздільник</td><td><code>SELECT CONCAT_WS('-', '2024', '07', '08');</code></td><td>2024-07-08</td></tr>
<tr><td><strong>DATALENGTH</strong></td><td>Повертає кількість байтів, які займає вираз</td><td><code>SELECT DATALENGTH(N'Київ');</code></td><td>8</td></tr>
<tr><td><strong>DIFFERENCE</strong></td><td>Порівнює два значення SOUNDEX і повертає число від 0 до 4</td><td><code>SELECT DIFFERENCE('Juice', 'Jucy');</code></td><td>4</td></tr>
<tr><td><strong>FORMAT</strong></td><td>Форматує значення за шаблоном і культурою</td><td><code>SELECT FORMAT(1234567.891, 'N2', 'uk-UA');</code></td><td>1 234 567,89</td></tr>
<tr><td><strong>LEFT</strong></td><td>Повертає задану кількість символів з початку рядка</td><td><code>SELECT LEFT('SQL Server', 3);</code></td><td>SQL</td></tr>
<tr><td><strong>LEN</strong></td><td>Повертає довжину рядка (без кінцевих пробілів)</td><td><code>SELECT LEN('SQL Server  ');</code></td><td>10</td></tr>
<tr><td><strong>LOWER</strong></td><td>Перетворює рядок на нижній регістр</td><td><code>SELECT LOWER('SQL Server');</code></td><td>sql server</td></tr>
<tr><td><strong>LTRIM</strong></td><td>Видаляє пробіли на початку рядка</td><td><code>SELECT LTRIM('   SQL');</code></td><td>SQL</td></tr>
<tr><td><strong>NCHAR</strong></td><td>Повертає символ Unicode за кодом</td><td><code>SELECT NCHAR(1028);</code></td><td>Є</td></tr>
<tr><td><strong>PATINDEX</strong></td><td>Повертає позицію першого входження шаблону</td><td><code>SELECT PATINDEX('%[0-9]%', 'abc123');</code></td><td>4</td></tr>
<tr><td><strong>QUOTENAME</strong></td><td>Бере рядок у роздільники, роблячи його коректним ідентифікатором</td><td><code>SELECT QUOTENAME('my table');</code></td><td>[my table]</td></tr>
<tr><td><strong>REPLACE</strong></td><td>Замінює всі входження підрядка іншим рядком</td><td><code>SELECT REPLACE('SQL Tutorial', 'Tutorial', 'Server');</code></td><td>SQL Server</td></tr>
<tr><td><strong>REPLICATE</strong></td><td>Повторює рядок задану кількість разів</td><td><code>SELECT REPLICATE('ab', 3);</code></td><td>ababab</td></tr>
<tr><td><strong>REVERSE</strong></td><td>Перевертає рядок</td><td><code>SELECT REVERSE('SQL');</code></td><td>LQS</td></tr>
<tr><td><strong>RIGHT</strong></td><td>Повертає задану кількість символів з кінця рядка</td><td><code>SELECT RIGHT('SQL Server', 6);</code></td><td>Server</td></tr>
<tr><td><strong>RTRIM</strong></td><td>Видаляє пробіли в кінці рядка</td><td><code>SELECT RTRIM('SQL   ') + '|';</code></td><td>SQL|</td></tr>
<tr><td><strong>SOUNDEX</strong></td><td>Повертає чотирисимвольний фонетичний код рядка</td><td><code>SELECT SOUNDEX('Juice');</code></td><td>J200</td></tr>
<tr><td><strong>SPACE</strong></td><td>Повертає рядок із заданої кількості пробілів</td><td><code>SELECT '[' + SPACE(3) + ']';</code></td><td>[   ]</td></tr>
<tr><td><strong>STR</strong></td><td>Перетворює число на рядок</td><td><code>SELECT STR(185.476, 6, 2);</code></td><td>185.48</td></tr>
<tr><td><strong>STRING_AGG</strong></td><td>Об'єднує значення рядків групи через роздільник (2017+)</td><td><code>SELECT (SELECT STRING_AGG(ShipperName, ', ') FROM Shippers);</code></td><td>Speedy Express, United Package, Federal Shipping</td></tr>
<tr><td><strong>STRING_SPLIT</strong></td><td>Таблична функція: розбиває рядок на рядки за роздільником (2016+)</td><td><code>SELECT (SELECT COUNT(*) FROM STRING_SPLIT('a,b,c', ','));</code></td><td>3</td></tr>
<tr><td><strong>STUFF</strong></td><td>Видаляє частину рядка і вставляє на її місце інший рядок</td><td><code>SELECT STUFF('SQL Tutorial', 1, 3, 'T-SQL');</code></td><td>T-SQL Tutorial</td></tr>
<tr><td><strong>SUBSTRING</strong></td><td>Повертає частину рядка</td><td><code>SELECT SUBSTRING('SQL Server', 5, 6);</code></td><td>Server</td></tr>
<tr><td><strong>TRANSLATE</strong></td><td>Посимвольно замінює символи (2017+)</td><td><code>SELECT TRANSLATE('2*[3+4]', '[]', '()');</code></td><td>2*(3+4)</td></tr>
<tr><td><strong>TRIM</strong></td><td>Видаляє пробіли (або задані символи) з обох кінців рядка (2017+)</td><td><code>SELECT '|' + TRIM('   SQL   ') + '|';</code></td><td>|SQL|</td></tr>
<tr><td><strong>UNICODE</strong></td><td>Повертає код Unicode першого символу</td><td><code>SELECT UNICODE(N'Ї');</code></td><td>1031</td></tr>
<tr><td><strong>UPPER</strong></td><td>Перетворює рядок на верхній регістр</td><td><code>SELECT UPPER('SQL Server');</code></td><td>SQL SERVER</td></tr>
</table></div>
