---
title: "Інші функції"
h1: "Функції перетворення та системні функції"
---

Функції перетворення типів, роботи з NULL, умовні та системні функції.

Колонка «Результат» отримана виконанням прикладу на SQL Server 2022 з демо-базою DemoShop.

<div class="table-scroll"><table>
<tr><th>Функція</th><th>Опис</th><th>Приклад</th><th>Результат</th></tr>
<tr><td><strong>CAST</strong></td><td>Перетворює значення в інший тип даних</td><td><code>SELECT CAST('25.65' AS DECIMAL(5,1));</code></td><td>25.7</td></tr>
<tr><td><strong>COALESCE</strong></td><td>Повертає перше значення зі списку, що не є NULL</td><td><code>SELECT COALESCE(NULL, NULL, 'SQL', 'Server');</code></td><td>SQL</td></tr>
<tr><td><strong>CONVERT</strong></td><td>Перетворює значення в інший тип (зі стилем форматування)</td><td><code>SELECT CONVERT(VARCHAR(10), CAST('2024-07-08' AS DATE), 104);</code></td><td>08.07.2024</td></tr>
<tr><td><strong>CURRENT_USER</strong></td><td>Ім'я поточного користувача бази даних</td><td><code>SELECT CURRENT_USER;</code></td><td>dbo</td></tr>
<tr><td><strong>DB_NAME</strong></td><td>Ім'я поточної (або заданої) бази даних</td><td><code>SELECT DB_NAME();</code></td><td>DemoShop</td></tr>
<tr><td><strong>CHOOSE</strong></td><td>Повертає елемент списку за індексом</td><td><code>SELECT CHOOSE(2, 'red', 'green', 'blue');</code></td><td>green</td></tr>
<tr><td><strong>GREATEST</strong></td><td>Найбільше значення зі списку (2022+)</td><td><code>SELECT GREATEST(5, 12, 3);</code></td><td>12</td></tr>
<tr><td><strong>IIF</strong></td><td>Повертає одне з двох значень залежно від умови</td><td><code>SELECT IIF(500 &lt; 1000, 'YES', 'NO');</code></td><td>YES</td></tr>
<tr><td><strong>ISNULL</strong></td><td>Повертає заміну, якщо вираз дорівнює NULL</td><td><code>SELECT ISNULL(NULL, 'SQL Server');</code></td><td>SQL Server</td></tr>
<tr><td><strong>ISNUMERIC</strong></td><td>Перевіряє, чи є вираз числом (1 або 0)</td><td><code>SELECT ISNUMERIC('4567');</code></td><td>1</td></tr>
<tr><td><strong>LEAST</strong></td><td>Найменше значення зі списку (2022+)</td><td><code>SELECT LEAST(5, 12, 3);</code></td><td>3</td></tr>
<tr><td><strong>NEWID</strong></td><td>Генерує новий унікальний ідентифікатор (GUID)</td><td><code>SELECT NEWID();</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>NULLIF</strong></td><td>Повертає NULL, якщо два вирази рівні</td><td><code>SELECT NULLIF(25, 25);</code></td><td><span class="null">NULL</span></td></tr>
<tr><td><strong>OBJECT_ID</strong></td><td>Ідентифікатор об'єкта бази даних за іменем</td><td><code>SELECT CASE WHEN OBJECT_ID('dbo.Customers') IS NOT NULL THEN 'exists' END;</code></td><td>exists</td></tr>
<tr><td><strong>SESSION_USER</strong></td><td>Ім'я користувача в поточному сеансі</td><td><code>SELECT SESSION_USER;</code></td><td>dbo</td></tr>
<tr><td><strong>SESSIONPROPERTY</strong></td><td>Значення параметра сеансу</td><td><code>SELECT SESSIONPROPERTY('ANSI_NULLS');</code></td><td>0x01000000</td></tr>
<tr><td><strong>SYSTEM_USER</strong></td><td>Ім'я логіна</td><td><code>SELECT SYSTEM_USER;</code></td><td>sa</td></tr>
<tr><td><strong>TRY_CAST</strong></td><td>Як CAST, але повертає NULL замість помилки</td><td><code>SELECT TRY_CAST('abc' AS INT);</code></td><td><span class="null">NULL</span></td></tr>
<tr><td><strong>TRY_CONVERT</strong></td><td>Як CONVERT, але повертає NULL замість помилки</td><td><code>SELECT TRY_CONVERT(DATE, '2024-13-45');</code></td><td><span class="null">NULL</span></td></tr>
<tr><td><strong>TRY_PARSE</strong></td><td>Перетворює рядок з урахуванням культури, NULL при помилці</td><td><code>SELECT TRY_PARSE('08.07.2024' AS DATE USING 'uk-UA');</code></td><td>2024-07-08</td></tr>
<tr><td><strong>USER_NAME</strong></td><td>Ім'я користувача бази даних за ідентифікатором</td><td><code>SELECT USER_NAME();</code></td><td>dbo</td></tr>
<tr><td><strong>@@ROWCOUNT</strong></td><td>Кількість рядків, оброблених останньою інструкцією</td><td><code>SELECT @@ROWCOUNT;</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>@@VERSION</strong></td><td>Версія SQL Server</td><td><code>SELECT @@VERSION;</code></td><td><span class="null">залежить від сервера</span></td></tr>
<tr><td><strong>JSON_VALUE</strong></td><td>Витягує скалярне значення з JSON</td><td><code>SELECT JSON_VALUE('{"city":"Kyiv"}', '$.city');</code></td><td>Kyiv</td></tr>
<tr><td><strong>ISJSON</strong></td><td>Перевіряє, чи є рядок коректним JSON</td><td><code>SELECT ISJSON('{"a":1}');</code></td><td>1</td></tr>
</table></div>
