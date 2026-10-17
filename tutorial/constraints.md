---
title: "Обмеження (Constraints)"
h1: "Обмеження (Constraints)"
---

Обмеження (constraints) — це правила для даних у таблиці.

Вони обмежують, які дані можна записати в таблицю, і тим самим забезпечують **точність і цілісність** даних. Якщо операція порушує обмеження, вона скасовується.

Обмеження можна задати під час створення таблиці (`CREATE TABLE`) або пізніше (`ALTER TABLE`).

## Синтаксис

```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ...
);
```

## Обмеження в SQL Server

| Обмеження | Опис |
|---|---|
| [`NOT NULL`](not-null.html) | Стовпець не може містити `NULL` |
| [`UNIQUE`](unique.html) | Усі значення в стовпці різні |
| [`PRIMARY KEY`](primary-key.html) | Поєднання `NOT NULL` і `UNIQUE`; однозначно ідентифікує рядок |
| [`FOREIGN KEY`](foreign-key.html) | Не дає порушити зв'язки між таблицями |
| [`CHECK`](check.html) | Значення повинні задовольняти умову |
| [`DEFAULT`](default.html) | Значення за замовчуванням, якщо інше не вказано |

Окремо існують [індекси](create-index.html) (`CREATE INDEX`) — вони пришвидшують пошук даних.

## Іменовані обмеження

Кожне обмеження в SQL Server має ім'я. Якщо не вказати його, сервер згенерує ім'я автоматично (на кшталт `PK__Persons__3214EC27A1B2C3D4`). Краще задавати імена явно — тоді обмеження легко змінити чи видалити:

<div class="example" markdown="1">

```sql
CREATE TABLE Employees2 (
    EmployeeID INT NOT NULL,
    Email      NVARCHAR(100) NOT NULL,
    Salary     DECIMAL(10,2) NOT NULL,
    HireDate   DATE NOT NULL
        CONSTRAINT DF_Employees2_HireDate DEFAULT (GETDATE()),
    CONSTRAINT PK_Employees2        PRIMARY KEY (EmployeeID),
    CONSTRAINT UQ_Employees2_Email  UNIQUE (Email),
    CONSTRAINT CK_Employees2_Salary CHECK (Salary > 0)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
Поширені префікси імен: `PK_` — первинний ключ, `FK_` — зовнішній ключ, `UQ_` — унікальність, `CK_` — перевірка, `DF_` — значення за замовчуванням, `IX_` — індекс.

Обмеження `DEFAULT` у `CREATE TABLE` задається лише на рівні стовпця (як для `HireDate` вище). Решту обмежень можна задавати як на рівні стовпця, так і окремими рядками в кінці визначення таблиці.
</div>

## Перегляд обмежень таблиці

<div class="example" markdown="1">

```sql
SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'OrderDetails';
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CONSTRAINT_NAME</th><th>CONSTRAINT_TYPE</th></tr>
<tr><td>PK__OrderDet__D3B9D30CAC23A275</td><td>PRIMARY KEY</td></tr>
<tr><td>FK__OrderDeta__Order__4BAC3F29</td><td>FOREIGN KEY</td></tr>
<tr><td>FK__OrderDeta__Produ__4CA06362</td><td>FOREIGN KEY</td></tr>
<tr><td>CK__OrderDeta__Quant__4D94879B</td><td>CHECK</td></tr>
</table></div>
<p class="result-more">Рядків: 4</p>
<!-- run:end -->

</div>
