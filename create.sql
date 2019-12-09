CREATE TABLE Clients(
client_id int NOT NULL PRIMARY KEY,
Client_name varchar(30)  NOT NULL,
Age int NOT NULL,
Money int NOT NULL,
Contact int NOT NULL,
Created timestamp
);
CREATE TABLE Tests(
    test_id int NOT NULL PRIMARY KEY,
    Price int NOT NULL ,
	Productor varchar(30)  NOT NULL, 
    Created timestamp,
	client_idIDFK int,
	FOREIGN KEY (client_idIDFK) REFERENCES Clients(client_id)
	);
CREATE TABLE Products (
	product_id int NOT NULL PRIMARY KEY,
	Product_name varchar(100) NOT NULL ,
	Product_price int NOT NULL,
	Created timestamp,
	test_idIDFK int,
	FOREIGN KEY (test_idIDFK) REFERENCES tests(test_id)
);
CREATE TABLE Shops(
    shop_id int NOT NULL PRIMARY KEY,
    Shop_name varchar(100) NOT NULL ,
    Locale varchar(50) NOT NULL,
	Shop_contact int NOT NULL,
	Created timestamp,
	product_idIDFK int,
	FOREIGN KEY (product_idIDFK) REFERENCES products(product_id)
); 
CREATE TABLE Workers(
    worker_id int NOT NULL PRIMARY KEY,
    Worker_name varchar(100) NOT NULL ,
    Birthday int NOT NULL,
	Email int NOT NULL,
	City varchar(100) NOT NULL,
	Created timestamp,
	shop_idIDFK int,
	FOREIGN KEY (shop_idIDFK) REFERENCES shops(shop_id)
);







