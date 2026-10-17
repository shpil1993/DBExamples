---
title: Головна
hide_title: true
---

<div class="hero" markdown="1">

# Підручник SQL Server

**Microsoft SQL Server** — одна з найпопулярніших реляційних систем керування базами даних. У цьому курсі ви крок за кроком вивчите мову **T-SQL** (Transact-SQL): від простих запитів `SELECT` до збережених процедур, тригерів і транзакцій.

Кожен урок містить пояснення, синтаксис і приклади з результатами, перевірені на SQL Server 2022.

<a class="btn btn-lg" href="{{ '/tutorial/home.html' | relative_url }}">Почати навчання ❯</a>

</div>

## Приклад

```sql
SELECT TOP (3) ProductName, Price
FROM Products
ORDER BY Price DESC;
```

Цей запит повертає три найдорожчі товари з таблиці `Products`. Уже скоро ви будете писати такі запити самостійно.

## Зміст курсу

<div class="toc-grid">
{% for s in site.data.nav %}
<div class="toc-card">
<h3>{{ s.section }}</h3>
<ol>
{% for p in s.pages %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ol>
</div>
{% endfor %}
</div>
