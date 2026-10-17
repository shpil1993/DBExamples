---
title: Демо-база даних
---

У всіх прикладах курсу використовується навчальна база даних **DemoShop** — спрощена версія відомої бази *Northwind*. Вона описує невеликий магазин продуктів: клієнтів, товари, замовлення, працівників тощо.

## Як створити базу

1. Завантажте скрипт: <a href="{{ '/assets/sql/demo-db.sql' | relative_url }}" download>demo-db.sql</a>.
2. Відкрийте його в SSMS або VS Code і виконайте повністю (F5).
   Або виконайте з командного рядка:

```bash
sqlcmd -S localhost,1433 -U sa -P "Str0ng!Passw0rd" -C -i demo-db.sql
```

Скрипт створює базу `DemoShop`. Якщо база з такою назвою вже існує, вона буде видалена й створена заново — так можна будь-коли повернути дані до початкового стану.

<div class="note" markdown="1">
Перед виконанням прикладів переконайтеся, що вибрано саме базу DemoShop: у SSMS — у списку баз на панелі інструментів, або командою `USE DemoShop;`
</div>

## Таблиці бази DemoShop

| Таблиця | Опис | Ключові стовпці |
|---|---|---|
| `Customers` | Клієнти | `CustomerID`, `CustomerName`, `City`, `Country` |
| `Orders` | Замовлення | `OrderID`, `CustomerID`, `EmployeeID`, `OrderDate`, `ShipperID` |
| `OrderDetails` | Рядки замовлень (які товари і скільки) | `OrderDetailID`, `OrderID`, `ProductID`, `Quantity` |
| `Products` | Товари | `ProductID`, `ProductName`, `SupplierID`, `CategoryID`, `Price` |
| `Categories` | Категорії товарів | `CategoryID`, `CategoryName` |
| `Suppliers` | Постачальники | `SupplierID`, `SupplierName`, `City`, `Country` |
| `Employees` | Працівники | `EmployeeID`, `LastName`, `FirstName`, `BirthDate`, `ManagerID` |
| `Shippers` | Служби доставки | `ShipperID`, `ShipperName`, `Phone` |

## Схема зв'язків

```text
Customers (CustomerID) ──< Orders (CustomerID)
Employees (EmployeeID) ──< Orders (EmployeeID)
Shippers  (ShipperID)  ──< Orders (ShipperID)
Orders    (OrderID)    ──< OrderDetails (OrderID)
Products  (ProductID)  ──< OrderDetails (ProductID)
Categories(CategoryID) ──< Products (CategoryID)
Suppliers (SupplierID) ──< Products (SupplierID)
Employees (EmployeeID) ──< Employees (ManagerID)
```

Знак `──<` означає зв'язок «один до багатьох»: наприклад, один клієнт може мати багато замовлень.

## Огляд даних

### Customers

```sql
SELECT * FROM Customers;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CustomerID</th><th>CustomerName</th><th>ContactName</th><th>Address</th><th>City</th><th>PostalCode</th><th>Country</th></tr>
<tr><td>1</td><td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Obere Str. 57</td><td>Berlin</td><td>12209</td><td>Germany</td></tr>
<tr><td>2</td><td>Ana Trujillo Emparedados y helados</td><td>Ana Trujillo</td><td>Avda. de la Constitución 2222</td><td>México D.F.</td><td>05021</td><td>Mexico</td></tr>
<tr><td>3</td><td>Antonio Moreno Taquería</td><td>Antonio Moreno</td><td>Mataderos 2312</td><td>México D.F.</td><td>05023</td><td>Mexico</td></tr>
<tr><td>4</td><td>Around the Horn</td><td>Thomas Hardy</td><td>120 Hanover Sq.</td><td>London</td><td>WA1 1DP</td><td>UK</td></tr>
<tr><td>5</td><td>Berglunds snabbköp</td><td>Christina Berglund</td><td>Berguvsvägen 8</td><td>Luleå</td><td>S-958 22</td><td>Sweden</td></tr>
<tr><td>6</td><td>Blauer See Delikatessen</td><td>Hanna Moos</td><td>Forsterstr. 57</td><td>Mannheim</td><td>68306</td><td>Germany</td></tr>
<tr><td>7</td><td>Blondel père et fils</td><td>Frédérique Citeaux</td><td>24, place Kléber</td><td>Strasbourg</td><td>67000</td><td>France</td></tr>
<tr><td>8</td><td>Bólido Comidas preparadas</td><td>Martín Sommer</td><td>C/ Araquil, 67</td><td>Madrid</td><td>28023</td><td>Spain</td></tr>
<tr><td>9</td><td>Bon app'</td><td>Laurence Lebihans</td><td>12, rue des Bouchers</td><td>Marseille</td><td>13008</td><td>France</td></tr>
<tr><td>10</td><td>Bottom-Dollar Marketse</td><td>Elizabeth Lincoln</td><td>23 Tsawassen Blvd.</td><td>Tsawassen</td><td>T2F 8M4</td><td>Canada</td></tr>
<tr><td>11</td><td>Kyiv Market</td><td>Olena Shevchenko</td><td>Khreshchatyk 22</td><td>Kyiv</td><td>01001</td><td>Ukraine</td></tr>
<tr><td>12</td><td>Lviv Coffee House</td><td>Taras Kovalenko</td><td>Rynok Sq. 10</td><td>Lviv</td><td>79008</td><td>Ukraine</td></tr>
<tr><td>13</td><td>Odesa Seafood</td><td><span class="null">NULL</span></td><td>Derybasivska 5</td><td>Odesa</td><td>65026</td><td>Ukraine</td></tr>
</table></div>
<p class="result-more">Рядків: 13</p>
<!-- run:end -->

### Products

```sql
SELECT * FROM Products;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>ProductID</th><th>ProductName</th><th>SupplierID</th><th>CategoryID</th><th>Unit</th><th>Price</th></tr>
<tr><td>1</td><td>Chais</td><td>1</td><td>1</td><td>10 boxes x 20 bags</td><td>18.00</td></tr>
<tr><td>2</td><td>Chang</td><td>1</td><td>1</td><td>24 - 12 oz bottles</td><td>19.00</td></tr>
<tr><td>3</td><td>Aniseed Syrup</td><td>1</td><td>2</td><td>12 - 550 ml bottles</td><td>10.00</td></tr>
<tr><td>4</td><td>Chef Anton's Cajun Seasoning</td><td>2</td><td>2</td><td>48 - 6 oz jars</td><td>22.00</td></tr>
<tr><td>5</td><td>Chef Anton's Gumbo Mix</td><td>2</td><td>2</td><td>36 boxes</td><td>21.35</td></tr>
<tr><td>6</td><td>Grandma's Boysenberry Spread</td><td>3</td><td>2</td><td>12 - 8 oz jars</td><td>25.00</td></tr>
<tr><td>7</td><td>Uncle Bob's Organic Dried Pears</td><td>3</td><td>7</td><td>12 - 1 lb pkgs.</td><td>30.00</td></tr>
<tr><td>8</td><td>Northwoods Cranberry Sauce</td><td>3</td><td>2</td><td>12 - 12 oz jars</td><td>40.00</td></tr>
<tr><td>9</td><td>Mishi Kobe Niku</td><td>4</td><td>6</td><td>18 - 500 g pkgs.</td><td>97.00</td></tr>
<tr><td>10</td><td>Ikura</td><td>4</td><td>8</td><td>12 - 200 ml jars</td><td>31.00</td></tr>
<tr><td>11</td><td>Queso Cabrales</td><td>5</td><td>4</td><td>1 kg pkg.</td><td>21.00</td></tr>
<tr><td>12</td><td>Queso Manchego La Pastora</td><td>5</td><td>4</td><td>10 - 500 g pkgs.</td><td>38.00</td></tr>
<tr><td>13</td><td>Pavlova</td><td>6</td><td>3</td><td>32 - 500 g boxes</td><td>17.45</td></tr>
<tr><td>14</td><td>Vegie-spread</td><td>6</td><td>2</td><td>15 - 625 g jars</td><td>43.90</td></tr>
<tr><td>15</td><td>Tunnbröd</td><td><span class="null">NULL</span></td><td>5</td><td>12 - 250 g pkgs.</td><td>9.00</td></tr>
</table></div>
<p class="result-more">Рядків: 15</p>
<!-- run:end -->

### Categories

```sql
SELECT * FROM Categories;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>CategoryID</th><th>CategoryName</th><th>Description</th></tr>
<tr><td>1</td><td>Beverages</td><td>Soft drinks, coffees, teas, beers, and ales</td></tr>
<tr><td>2</td><td>Condiments</td><td>Sweet and savory sauces, relishes, spreads, and seasonings</td></tr>
<tr><td>3</td><td>Confections</td><td>Desserts, candies, and sweet breads</td></tr>
<tr><td>4</td><td>Dairy Products</td><td>Cheeses</td></tr>
<tr><td>5</td><td>Grains/Cereals</td><td>Breads, crackers, pasta, and cereal</td></tr>
<tr><td>6</td><td>Meat/Poultry</td><td>Prepared meats</td></tr>
<tr><td>7</td><td>Produce</td><td>Dried fruit and bean curd</td></tr>
<tr><td>8</td><td>Seafood</td><td>Seaweed and fish</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

### Employees

```sql
SELECT * FROM Employees;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>EmployeeID</th><th>LastName</th><th>FirstName</th><th>BirthDate</th><th>ManagerID</th></tr>
<tr><td>1</td><td>Fuller</td><td>Andrew</td><td>1952-02-19</td><td><span class="null">NULL</span></td></tr>
<tr><td>2</td><td>Davolio</td><td>Nancy</td><td>1968-12-08</td><td>1</td></tr>
<tr><td>3</td><td>Leverling</td><td>Janet</td><td>1963-08-30</td><td>1</td></tr>
<tr><td>4</td><td>Peacock</td><td>Margaret</td><td>1958-09-19</td><td>1</td></tr>
<tr><td>5</td><td>Buchanan</td><td>Steven</td><td>1955-03-04</td><td>1</td></tr>
<tr><td>6</td><td>Suyama</td><td>Michael</td><td>1963-07-02</td><td>5</td></tr>
<tr><td>7</td><td>King</td><td>Robert</td><td>1960-05-29</td><td>5</td></tr>
</table></div>
<p class="result-more">Рядків: 7</p>
<!-- run:end -->

### Shippers

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

### Suppliers

```sql
SELECT * FROM Suppliers;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>SupplierID</th><th>SupplierName</th><th>ContactName</th><th>City</th><th>Country</th><th>Phone</th></tr>
<tr><td>1</td><td>Exotic Liquid</td><td>Charlotte Cooper</td><td>London</td><td>UK</td><td>(171) 555-2222</td></tr>
<tr><td>2</td><td>New Orleans Cajun Delights</td><td>Shelley Burke</td><td>New Orleans</td><td>USA</td><td>(100) 555-4822</td></tr>
<tr><td>3</td><td>Grandma Kelly's Homestead</td><td>Regina Murphy</td><td>Ann Arbor</td><td>USA</td><td>(313) 555-5735</td></tr>
<tr><td>4</td><td>Tokyo Traders</td><td>Yoshi Nagase</td><td>Tokyo</td><td>Japan</td><td>(03) 3555-5011</td></tr>
<tr><td>5</td><td>Cooperativa de Quesos 'Las Cabras'</td><td>Antonio del Valle Saavedra</td><td>Oviedo</td><td>Spain</td><td>(98) 598 76 54</td></tr>
<tr><td>6</td><td>Pavlova, Ltd.</td><td>Ian Devling</td><td>Melbourne</td><td>Australia</td><td>(03) 444-2343</td></tr>
</table></div>
<p class="result-more">Рядків: 6</p>
<!-- run:end -->

### Orders

```sql
SELECT * FROM Orders;
```

<!-- run:start rows=20 -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderID</th><th>CustomerID</th><th>EmployeeID</th><th>OrderDate</th><th>ShipperID</th></tr>
<tr><td>10248</td><td>4</td><td>5</td><td>2024-07-04</td><td>3</td></tr>
<tr><td>10249</td><td>1</td><td>6</td><td>2024-07-05</td><td>1</td></tr>
<tr><td>10250</td><td>3</td><td>4</td><td>2024-07-08</td><td>2</td></tr>
<tr><td>10251</td><td>7</td><td>3</td><td>2024-07-08</td><td>1</td></tr>
<tr><td>10252</td><td>2</td><td>4</td><td>2024-07-09</td><td>2</td></tr>
<tr><td>10253</td><td>4</td><td>3</td><td>2024-07-10</td><td>2</td></tr>
<tr><td>10254</td><td>5</td><td>4</td><td>2024-07-11</td><td>2</td></tr>
<tr><td>10255</td><td>8</td><td>4</td><td>2024-07-12</td><td>3</td></tr>
<tr><td>10256</td><td>9</td><td>3</td><td>2024-08-15</td><td>1</td></tr>
<tr><td>10257</td><td>11</td><td>2</td><td>2024-09-01</td><td>2</td></tr>
<tr><td>10258</td><td>11</td><td>2</td><td>2024-09-20</td><td>3</td></tr>
<tr><td>10259</td><td>12</td><td>7</td><td>2024-10-03</td><td>1</td></tr>
<tr><td>10260</td><td>1</td><td>2</td><td>2024-11-14</td><td>2</td></tr>
<tr><td>10261</td><td>10</td><td><span class="null">NULL</span></td><td>2024-12-02</td><td>1</td></tr>
</table></div>
<p class="result-more">Рядків: 14</p>
<!-- run:end -->

### OrderDetails (перші рядки)

```sql
SELECT TOP (8) * FROM OrderDetails;
```

<!-- run:start -->
<div class="result-label">Результат:</div>
<div class="table-scroll"><table>
<tr><th>OrderDetailID</th><th>OrderID</th><th>ProductID</th><th>Quantity</th></tr>
<tr><td>1</td><td>10248</td><td>11</td><td>12</td></tr>
<tr><td>2</td><td>10248</td><td>9</td><td>10</td></tr>
<tr><td>3</td><td>10248</td><td>14</td><td>5</td></tr>
<tr><td>4</td><td>10249</td><td>13</td><td>9</td></tr>
<tr><td>5</td><td>10249</td><td>1</td><td>40</td></tr>
<tr><td>6</td><td>10250</td><td>1</td><td>10</td></tr>
<tr><td>7</td><td>10250</td><td>2</td><td>35</td></tr>
<tr><td>8</td><td>10250</td><td>10</td><td>15</td></tr>
</table></div>
<p class="result-more">Рядків: 8</p>
<!-- run:end -->

<div class="note" markdown="1">
Зверніть увагу на кілька особливостей даних, які знадобляться в уроках: у клієнта *Odesa Seafood* не вказано `ContactName` (значення `NULL`), у замовлення 10261 не вказано працівника, а в товару *Tunnbröd* — постачальника. Деякі клієнти (наприклад, *Blauer See Delikatessen*) ще не мають жодного замовлення.
</div>
