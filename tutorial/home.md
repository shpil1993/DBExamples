---
title: "SQL Server: Головна"
h1: Підручник SQL Server
---

**SQL Server** — це система керування реляційними базами даних (СКБД) від компанії Microsoft.

SQL Server використовують для зберігання даних вебсайтів, бізнес-застосунків, аналітичних систем і сховищ даних.

У цьому підручнику ви вивчите **T-SQL** (Transact-SQL) — діалект мови SQL, який використовується в SQL Server.

## Приклади в кожному розділі

Кожен розділ містить приклади, які можна виконати у власній копії SQL Server. Під більшістю прикладів показано результат, який повертає сервер.

<div class="example" markdown="1">

### Приклад

Вибрати всіх клієнтів з Німеччини:

```sql
SELECT CustomerName, City, Country
FROM Customers
WHERE Country = N'Germany';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerName</th><th>City</th><th>Country</th></tr>
<tr><td>Alfreds Futterkiste</td><td>Berlin</td><td>Germany</td></tr>
<tr><td>Blauer See Delikatessen</td><td>Mannheim</td><td>Germany</td></tr>
</table></div>
<p class="result-more">Рядків: 2</p>
<!-- run:end -->

</div>

## Як працювати з курсом

1. Встановіть SQL Server і інструмент для запитів — див. розділ [Встановлення та інструменти](install.html).
2. Створіть навчальну базу даних за допомогою скрипту з розділу [Демо-база даних](demo-db.html).
3. Проходьте уроки по порядку — кнопки **«Попередній»** та **«Наступний»** вгорі й унизу кожної сторінки.
4. Виконуйте приклади самостійно та змінюйте їх, щоб краще зрозуміти, як вони працюють.

## Довідники

Окрім уроків, курс містить довідники:

* [Типи даних SQL Server](data-types.html)
* [Рядкові функції](string-functions.html)
* [Числові функції](numeric-functions.html)
* [Функції дати й часу](date-functions.html)
* [Інші функції](advanced-functions.html) (перетворення типів, системні функції)
* [Ключові слова](keywords.html)

<div class="note" markdown="1">
**Примітка.** Курс орієнтований на SQL Server 2019 і новіші версії (включно з SQL Server 2022 та Azure SQL Database). Більшість прикладів працює й у старіших версіях. Якщо функція з'явилася лише в новій версії, це вказано окремо.
</div>
