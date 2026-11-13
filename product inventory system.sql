--- creating database ---
create database product_db;
--- use database---
use product_db;
--- create table---
create table products
(id int auto_increment primary key,
name varchar(100),
price decimal(10,2),
quantity int);

select*from products;