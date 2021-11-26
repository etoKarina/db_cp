CREATE TABLE Product (
  idProduct INT PRIMARY KEY,
  pName VARCHAR(50),
  pType VARCHAR(50),
  pPrice NUMERIC,
  pExpDate INT
);

CREATE TABLE Storage (
  idStorage INT PRIMARY KEY,
  sType VARCHAR(50),
  sCount INT,
  sDate INT,
  idProd INT
);

CREATE TABLE Dish (
  idDish INT PRIMARY KEY,
  dName VARCHAR(50),
  dPrice NUMERIC,
  dDescription VARCHAR(150)
);

CREATE TABLE Consists (
    idDish INT,
    idProduct INT,
    PRIMARY KEY (idDish, idProduct)
);