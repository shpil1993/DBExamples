---
title: "FOREIGN KEY"
h1: "Обмеження FOREIGN KEY"
---

Обмеження `FOREIGN KEY` (зовнішній ключ) не дає виконати дії, які зруйнують зв'язки між таблицями.

**Зовнішній ключ** — це поле (або набір полів) в одній таблиці, яке посилається на `PRIMARY KEY` (або `UNIQUE`) в іншій таблиці.

* Таблиця із зовнішнім ключем називається **дочірньою** (child).
* Таблиця з первинним ключем — **батьківською** (referenced, parent).

## Приклад зв'язку

У демо-базі стовпець `Orders.CustomerID` посилається на `Customers.CustomerID`:

```sql
SELECT TOP (3) OrderID, CustomerID FROM Orders;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerID</th></tr>
<tr><td>10248</td><td>4</td></tr>
<tr><td>10249</td><td>1</td></tr>
<tr><td>10250</td><td>3</td></tr>
</table></div>
<p class="result-more">Рядків: 3</p>
<!-- run:end -->

`FOREIGN KEY` не дозволить додати в `Orders` замовлення з неіснуючим `CustomerID`:

<div class="example" markdown="1">

```sql
INSERT INTO Orders (CustomerID, OrderDate) VALUES (999, '2024-12-31');
```

</div>

```text
The INSERT statement conflicted with the FOREIGN KEY constraint "FK__Orders__Customer__...".
The conflict occurred in database "DemoShop", table "dbo.Customers", column 'CustomerID'.
```

## FOREIGN KEY у CREATE TABLE

<div class="example" markdown="1">

```sql
CREATE TABLE Orders2 (
    OrderID     INT NOT NULL PRIMARY KEY,
    OrderNumber INT NOT NULL,
    CustomerID  INT FOREIGN KEY REFERENCES Customers(CustomerID)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

Іменований зовнішній ключ (і ключ з кількох стовпців):

<div class="example" markdown="1">

```sql
CREATE TABLE Orders2 (
    OrderID     INT NOT NULL,
    OrderNumber INT NOT NULL,
    CustomerID  INT,
    CONSTRAINT PK_Orders2 PRIMARY KEY (OrderID),
    CONSTRAINT FK_Orders2_Customers FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

## FOREIGN KEY в ALTER TABLE

```sql
ALTER TABLE Orders2
ADD CONSTRAINT FK_Orders2_Customers
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID);
```

## Видалення FOREIGN KEY

```sql
ALTER TABLE Orders2
DROP CONSTRAINT FK_Orders2_Customers;
```

## Каскадні дії: ON DELETE та ON UPDATE

Можна вказати, що робити з дочірніми рядками, коли батьківський рядок видаляється або змінюється:

| Дія | Опис |
|---|---|
| `NO ACTION` | Заборонити операцію (за замовчуванням) |
| `CASCADE` | Видалити/оновити дочірні рядки разом з батьківським |
| `SET NULL` | Встановити `NULL` у зовнішньому ключі |
| `SET DEFAULT` | Встановити значення за замовчуванням |

<div class="example" markdown="1">

При видаленні замовлення автоматично видаляти його рядки:

```sql
CREATE TABLE OrderLines (
    LineID  INT IDENTITY PRIMARY KEY,
    OrderID INT NOT NULL,
    Product NVARCHAR(100),
    CONSTRAINT FK_OrderLines_Orders FOREIGN KEY (OrderID)
        REFERENCES Orders(OrderID)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<p class="result-more">Команди виконано успішно.</p>
<!-- run:end -->

</div>

<div class="note" markdown="1">
SQL Server **не** створює автоматично індекс для стовпця зовнішнього ключа (на відміну від MySQL). Для швидких JOIN і видалень рекомендується створити такий індекс самостійно:

```sql
CREATE INDEX IX_Orders_CustomerID ON Orders(CustomerID);
```
</div>
