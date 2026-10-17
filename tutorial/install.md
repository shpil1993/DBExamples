---
title: "Встановлення та інструменти"
---

Щоб виконувати приклади з курсу, вам потрібні дві речі:

1. **Сервер** — сам SQL Server, який зберігає дані й виконує запити.
2. **Клієнт** — програма, у якій ви пишете запити й бачите результати.

## Варіант 1. SQL Server Developer або Express (Windows)

1. Завантажте інсталятор зі сторінки [SQL Server Downloads](https://www.microsoft.com/sql-server/sql-server-downloads).
2. Оберіть безкоштовну редакцію **Developer** (усі можливості, лише для розробки) або **Express** (легка версія).
3. Запустіть інсталятор і виберіть тип встановлення **Basic**.
4. Після завершення запам'ятайте ім'я екземпляра сервера, наприклад `localhost` або `localhost\SQLEXPRESS`.

## Варіант 2. SQL Server у Docker (Windows, macOS, Linux)

Якщо у вас встановлено Docker, SQL Server можна запустити однією командою:

```bash
docker run -d --name sqlserver \
  -e "ACCEPT_EULA=Y" \
  -e "MSSQL_SA_PASSWORD=Str0ng!Passw0rd" \
  -p 1433:1433 \
  mcr.microsoft.com/mssql/server:2022-latest
```

Після запуску сервер доступний за адресою `localhost,1433`. Користувач — `sa`, пароль — той, що ви вказали в `MSSQL_SA_PASSWORD`.

<div class="warn" markdown="1">
Пароль користувача `sa` має бути складним: щонайменше 8 символів, великі й малі літери, цифри та спецсимволи. Інакше контейнер не запуститься.
</div>

## Варіант 3. Azure SQL Database

У хмарі Microsoft Azure можна створити базу даних Azure SQL (є безкоштовний рівень). Синтаксис T-SQL майже повністю збігається із SQL Server.

## Клієнтські інструменти

| Інструмент | Платформа | Опис |
|---|---|---|
| **SQL Server Management Studio (SSMS)** | Windows | Основний інструмент адміністрування й розробки |
| **Visual Studio Code** + розширення **SQL Server (mssql)** | Windows, macOS, Linux | Легкий редактор із підсвічуванням і виконанням запитів |
| **sqlcmd** | Windows, macOS, Linux | Утиліта командного рядка |

### Підключення в SSMS

1. Запустіть SSMS.
2. У вікні **Connect to Server** вкажіть **Server name**: `localhost` (або `localhost,1433` для Docker).
3. **Authentication**: *Windows Authentication* для локального сервера або *SQL Server Authentication* (логін `sa`) для Docker.
4. Натисніть **Connect**, потім **New Query** — відкриється вікно для запитів.
5. Напишіть запит і натисніть **F5** (або кнопку **Execute**).

### Підключення через sqlcmd

```bash
sqlcmd -S localhost,1433 -U sa -P "Str0ng!Passw0rd" -C
```

Після підключення введіть запит і рядок `GO`, щоб його виконати:

```sql
SELECT @@VERSION;
GO
```

Функція `@@VERSION` повертає версію сервера.

## Наступний крок

Тепер створіть навчальну базу даних — перейдіть до розділу [Демо-база даних](demo-db.html).
