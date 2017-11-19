--Note: This schema is written in SQLite.

CREATE TABLE User (
  UserID INTEGER PRIMARY KEY,
  Username TEXT NOT NULL UNIQUE,
  Password TEXT NOT NULL,
  Picture BLOB,
  Permissions TEXT NOT NULL REFERENCES UserPermissions(Type)
);

--Enumeration--
CREATE TABLE UserPermissions (
  Type TEXT PRIMARY KEY,
  Seq INTEGER UNIQUE
);

INSERT INTO UserPermissions VALUES ('MANAGER', 1);
INSERT INTO UserPermissions VALUES ('CASHIER', 2);
--End Enumeration

CREATE TABLE Customer (
  CustomerID INTEGER PRIMARY KEY,
  Name TEXT
);

CREATE TABLE Payment (
  PaymentID INTEGER PRIMARY KEY,
  OrderID INTEGER NOT NULL REFERENCES "Order"(OrderID),
  Type TEXT NOT NULL REFERENCES PaymentMethod(Type),
  Amount DECIMAL(9,2) NOT NULL
);

--Enumeration--
CREATE TABLE PaymentMethod (
  Type TEXT PRIMARY KEY,
  Seq INTEGER UNIQUE
);

INSERT INTO PaymentMethod VALUES ('CASH', 1);
INSERT INTO PaymentMethod VALUES ('CHECK', 2);
INSERT INTO PaymentMethod VALUES ('DEBIT', 3);
INSERT INTO PaymentMethod VALUES ('CREDIT', 4);
--End Enumeration

CREATE TABLE Product (
  ProductID INTEGER PRIMARY KEY,
  Name TEXT NOT NULL,
  Quantity INTEGER NOT NULL,
  Price DECIMAL(9,2) NOT NULL,
  Provider TEXT NOT NULL,
  ProviderContact TEXT
);

CREATE TABLE "Order" (
  OrderID INTEGER PRIMARY KEY,
  EmployeeID INTEGER NOT NULL REFERENCES User(UserID),
  CustomerID INTEGER NOT NULL REFERENCES Customer(CustomerID),
  Total DECIMAL(9,2) DEFAULT 0.00,
  Date DATE DEFAULT (date('now'))
);

CREATE TABLE OrderLine (
  OrderLineID INTEGER PRIMARY KEY,
  OrderID INTEGER NOT NULL REFERENCES "Order"(OrderID),
  ProductID INTEGER NOT NULL REFERENCES Product(ProductID),
  Quantity INTEGER DEFAULT 1,
  Price DECIMAL(9,2),
  Cost DECIMAL(9,2)
);

--Data from Iteration 1
INSERT INTO Product
    VALUES (1, 'Apple', 10, 1.00, 'Food, Inc.', '555-555-5555');
INSERT INTO Product
    VALUES (2, 'Banana', 30, 1.50, 'Food, Inc.', '555-555-5555');
INSERT INTO Product
    VALUES (3, 'Milk', 8, 3.00, 'Fake Farms', '111-111-1111');
INSERT INTO Product
    VALUES (4, 'Orange Juice', 10, 2.00, 'Food Inc.', '555-555-5555');
INSERT INTO Product
    VALUES (5, 'Chocolate Bar', 30, 2.50, 'Confectionary Co.', '333-333-3333');

--More sample data
INSERT INTO User
    VALUES (1, 'Fred Smith', 'manager', 'password', NULL, 'MANAGER');
INSERT INTO User
    VALUES (2, 'John Smith', 'cashier', 'password', NULL, 'CASHIER');
INSERT INTO Customer
    VALUES (1, 'Clark Kent');
INSERT INTO "Order"
    VALUES (1, 2, 1, 3.00, DEFAULT);
INSERT INTO OrderLine
    VALUES (1, 1, 1, 3, 1.00, 3.00);
INSERT INTO Payment
    VALUES (1, 1, 'CASH', 3.00);