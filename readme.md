# Product Inventory Management System

## Project Description
A console-based Product Inventory Management System developed using Python and MySQL to manage products, prices, and stock quantities. It supports product addition, price updates, stock management, sales tracking, and low-stock identification.

## Features
- **Add Product:** Add new products with name, price, and quantity.
- **Update Price:** Update the price of existing products.
- **Add Stock:** Increase product quantities.
- **Sell Product:** Reduce stock quantities after sales while checking stock availability.
- **View Products:** Display all available products.
- **Low Stock Alert:** Identify products with quantities below 20.

## Technologies Used
- Python
- MySQL
- MySQL Connector/Python
- python-dotenv

## Database Structure

Database: `product_db`

### Products Table
Stores product information:
- product_id
- name
- price
- quantity

## Installation and Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create the Database
Execute the SQL commands from the database SQL file using MySQL Workbench.

### 3. Configure Environment Variables
Create a `.env` file using `.env.example` as a reference.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=product_db
```

### 5. Run the Application
```bash
python main.py
```

## Learning Outcomes
- Practiced Python functions and control flow.
- Implemented MySQL database connectivity.
- Performed CRUD operations using SQL.
- Practiced stock updates and inventory tracking.
- Implemented conditional checks for stock availability.
- Used SQL queries to identify low-stock products.

