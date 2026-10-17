/*
  Демо-база даних DemoShop для курсу "SQL Server"
  Запустіть цей скрипт у SSMS, VS Code (розширення mssql) або sqlcmd.
  Скрипт видаляє і створює базу DemoShop заново.
*/
USE master;
GO

IF DB_ID(N'DemoShop') IS NOT NULL
BEGIN
    ALTER DATABASE DemoShop SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE DemoShop;
END
GO

CREATE DATABASE DemoShop;
GO

USE DemoShop;
GO

CREATE TABLE Categories (
    CategoryID   INT IDENTITY(1,1) PRIMARY KEY,
    CategoryName NVARCHAR(50)  NOT NULL,
    Description  NVARCHAR(200) NULL
);

CREATE TABLE Suppliers (
    SupplierID   INT IDENTITY(1,1) PRIMARY KEY,
    SupplierName NVARCHAR(100) NOT NULL,
    ContactName  NVARCHAR(100) NULL,
    City         NVARCHAR(50)  NULL,
    Country      NVARCHAR(50)  NULL,
    Phone        NVARCHAR(30)  NULL
);

CREATE TABLE Customers (
    CustomerID   INT IDENTITY(1,1) PRIMARY KEY,
    CustomerName NVARCHAR(100) NOT NULL,
    ContactName  NVARCHAR(100) NULL,
    Address      NVARCHAR(200) NULL,
    City         NVARCHAR(50)  NULL,
    PostalCode   NVARCHAR(20)  NULL,
    Country      NVARCHAR(50)  NULL
);

CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    LastName   NVARCHAR(50) NOT NULL,
    FirstName  NVARCHAR(50) NOT NULL,
    BirthDate  DATE         NULL,
    ManagerID  INT          NULL REFERENCES Employees(EmployeeID)
);

CREATE TABLE Shippers (
    ShipperID   INT IDENTITY(1,1) PRIMARY KEY,
    ShipperName NVARCHAR(100) NOT NULL,
    Phone       NVARCHAR(30)  NULL
);

CREATE TABLE Products (
    ProductID   INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    SupplierID  INT NULL REFERENCES Suppliers(SupplierID),
    CategoryID  INT NULL REFERENCES Categories(CategoryID),
    Unit        NVARCHAR(50)  NULL,
    Price       DECIMAL(10,2) NOT NULL DEFAULT 0
);

CREATE TABLE Orders (
    OrderID    INT IDENTITY(10248,1) PRIMARY KEY,
    CustomerID INT  NULL REFERENCES Customers(CustomerID),
    EmployeeID INT  NULL REFERENCES Employees(EmployeeID),
    OrderDate  DATE NOT NULL,
    ShipperID  INT  NULL REFERENCES Shippers(ShipperID)
);

CREATE TABLE OrderDetails (
    OrderDetailID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID       INT NOT NULL REFERENCES Orders(OrderID),
    ProductID     INT NOT NULL REFERENCES Products(ProductID),
    Quantity      INT NOT NULL CHECK (Quantity > 0)
);
GO

INSERT INTO Categories (CategoryName, Description) VALUES
(N'Beverages',      N'Soft drinks, coffees, teas, beers, and ales'),
(N'Condiments',     N'Sweet and savory sauces, relishes, spreads, and seasonings'),
(N'Confections',    N'Desserts, candies, and sweet breads'),
(N'Dairy Products', N'Cheeses'),
(N'Grains/Cereals', N'Breads, crackers, pasta, and cereal'),
(N'Meat/Poultry',   N'Prepared meats'),
(N'Produce',        N'Dried fruit and bean curd'),
(N'Seafood',        N'Seaweed and fish');

INSERT INTO Suppliers (SupplierName, ContactName, City, Country, Phone) VALUES
(N'Exotic Liquid',                  N'Charlotte Cooper', N'London',     N'UK',        N'(171) 555-2222'),
(N'New Orleans Cajun Delights',     N'Shelley Burke',    N'New Orleans', N'USA',       N'(100) 555-4822'),
(N'Grandma Kelly''s Homestead',     N'Regina Murphy',    N'Ann Arbor',   N'USA',       N'(313) 555-5735'),
(N'Tokyo Traders',                  N'Yoshi Nagase',     N'Tokyo',       N'Japan',     N'(03) 3555-5011'),
(N'Cooperativa de Quesos ''Las Cabras''', N'Antonio del Valle Saavedra', N'Oviedo', N'Spain', N'(98) 598 76 54'),
(N'Pavlova, Ltd.',                  N'Ian Devling',      N'Melbourne',   N'Australia', N'(03) 444-2343');

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) VALUES
(N'Alfreds Futterkiste',                 N'Maria Anders',       N'Obere Str. 57',                 N'Berlin',      N'12209',    N'Germany'),
(N'Ana Trujillo Emparedados y helados',  N'Ana Trujillo',       N'Avda. de la Constitución 2222', N'México D.F.', N'05021',    N'Mexico'),
(N'Antonio Moreno Taquería',             N'Antonio Moreno',     N'Mataderos 2312',                N'México D.F.', N'05023',    N'Mexico'),
(N'Around the Horn',                     N'Thomas Hardy',       N'120 Hanover Sq.',               N'London',      N'WA1 1DP',  N'UK'),
(N'Berglunds snabbköp',                  N'Christina Berglund', N'Berguvsvägen 8',                N'Luleå',       N'S-958 22', N'Sweden'),
(N'Blauer See Delikatessen',             N'Hanna Moos',         N'Forsterstr. 57',                N'Mannheim',    N'68306',    N'Germany'),
(N'Blondel père et fils',                N'Frédérique Citeaux', N'24, place Kléber',              N'Strasbourg',  N'67000',    N'France'),
(N'Bólido Comidas preparadas',           N'Martín Sommer',      N'C/ Araquil, 67',                N'Madrid',      N'28023',    N'Spain'),
(N'Bon app''',                           N'Laurence Lebihans',  N'12, rue des Bouchers',          N'Marseille',   N'13008',    N'France'),
(N'Bottom-Dollar Marketse',              N'Elizabeth Lincoln',  N'23 Tsawassen Blvd.',            N'Tsawassen',   N'T2F 8M4',  N'Canada'),
(N'Kyiv Market',                         N'Olena Shevchenko',   N'Khreshchatyk 22',               N'Kyiv',        N'01001',    N'Ukraine'),
(N'Lviv Coffee House',                   N'Taras Kovalenko',    N'Rynok Sq. 10',                  N'Lviv',        N'79008',    N'Ukraine'),
(N'Odesa Seafood',                       NULL,                  N'Derybasivska 5',                N'Odesa',       N'65026',    N'Ukraine');

INSERT INTO Employees (LastName, FirstName, BirthDate, ManagerID) VALUES
(N'Fuller',    N'Andrew',   '1952-02-19', NULL),
(N'Davolio',   N'Nancy',    '1968-12-08', 1),
(N'Leverling', N'Janet',    '1963-08-30', 1),
(N'Peacock',   N'Margaret', '1958-09-19', 1),
(N'Buchanan',  N'Steven',   '1955-03-04', 1),
(N'Suyama',    N'Michael',  '1963-07-02', 5),
(N'King',      N'Robert',   '1960-05-29', 5);

INSERT INTO Shippers (ShipperName, Phone) VALUES
(N'Speedy Express',   N'(503) 555-9831'),
(N'United Package',   N'(503) 555-3199'),
(N'Federal Shipping', N'(503) 555-9931');

INSERT INTO Products (ProductName, SupplierID, CategoryID, Unit, Price) VALUES
(N'Chais',                        1, 1, N'10 boxes x 20 bags',    18.00),
(N'Chang',                        1, 1, N'24 - 12 oz bottles',    19.00),
(N'Aniseed Syrup',                1, 2, N'12 - 550 ml bottles',   10.00),
(N'Chef Anton''s Cajun Seasoning', 2, 2, N'48 - 6 oz jars',       22.00),
(N'Chef Anton''s Gumbo Mix',      2, 2, N'36 boxes',              21.35),
(N'Grandma''s Boysenberry Spread', 3, 2, N'12 - 8 oz jars',       25.00),
(N'Uncle Bob''s Organic Dried Pears', 3, 7, N'12 - 1 lb pkgs.',   30.00),
(N'Northwoods Cranberry Sauce',   3, 2, N'12 - 12 oz jars',       40.00),
(N'Mishi Kobe Niku',              4, 6, N'18 - 500 g pkgs.',      97.00),
(N'Ikura',                        4, 8, N'12 - 200 ml jars',      31.00),
(N'Queso Cabrales',               5, 4, N'1 kg pkg.',             21.00),
(N'Queso Manchego La Pastora',    5, 4, N'10 - 500 g pkgs.',      38.00),
(N'Pavlova',                      6, 3, N'32 - 500 g boxes',      17.45),
(N'Vegie-spread',                 6, 2, N'15 - 625 g jars',       43.90),
(N'Tunnbröd',                  NULL, 5, N'12 - 250 g pkgs.',       9.00);

INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES
(4,  5, '2024-07-04', 3),
(1,  6, '2024-07-05', 1),
(3,  4, '2024-07-08', 2),
(7,  3, '2024-07-08', 1),
(2,  4, '2024-07-09', 2),
(4,  3, '2024-07-10', 2),
(5,  4, '2024-07-11', 2),
(8,  4, '2024-07-12', 3),
(9,  3, '2024-08-15', 1),
(11, 2, '2024-09-01', 2),
(11, 2, '2024-09-20', 3),
(12, 7, '2024-10-03', 1),
(1,  2, '2024-11-14', 2),
(10, NULL, '2024-12-02', 1);

INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES
(10248, 11, 12), (10248, 9, 10), (10248, 14, 5),
(10249, 13, 9),  (10249, 1, 40),
(10250, 1, 10),  (10250, 2, 35), (10250, 10, 15),
(10251, 7, 6),   (10251, 12, 15),
(10252, 3, 40),  (10252, 6, 25),
(10253, 4, 20),  (10253, 8, 42),
(10254, 15, 15),
(10255, 2, 20),  (10255, 5, 35), (10255, 11, 25),
(10256, 13, 15),
(10257, 1, 25),  (10257, 9, 6),
(10258, 10, 4),  (10258, 2, 12),
(10259, 1, 30),
(10260, 12, 10), (10260, 14, 3),
(10261, 6, 18);
GO

PRINT N'Базу даних DemoShop створено успішно.';
