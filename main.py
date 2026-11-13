#PRODUCT INVENTORY SYSTEM

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

#function to create connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection

    except mysql.connector.Error as error:
        print("database connection error:", error)
        return None

#function to add product
def add_product():
    connection=create_connection()
    cursor=connection.cursor()
    name=input("enter the product name:")
    cursor.execute("select*from products where name=%s",(name,))    
    product=cursor.fetchone()
    if product:
        print("product already exists.")
        
    else:
        price=input("enter the product price:")
        quantity=input("enter the quantity of product:")
        query="""
        insert into products(name,price,quantity)
        values(%s,%s,%s)
        """
        cursor.execute(query,(name,price,quantity))
        connection.commit()
        print("product added successfully.")
        cursor.close()
        connection.close()
#function to update price
def update_product():
    connection=create_connection()
    cursor=connection.cursor()
    name=input("enter product name to update:")
    cursor.execute("select*from products where name=%s",(name,))
    product=cursor.fetchone()
    if product:
        new_price=input('enter new price:')
        cursor.execute("update products set price=%s where name=%s",
        (new_price,name))
        connection.commit()
        print("pruduct updated successfully.")
    else:
        print("no such record found.")  
        connection.close()
        cursor.close()
#function to add stock
def add_stock():
    connection=create_connection()
    cursor=connection.cursor()
    name=input("enter the product name:")
    cursor.execute("select*from products where name=%s",(name,))
    product=cursor.fetchone()
    if product:
        stock=int(input("enter the quantity to add:"))
        query="""update products set quantity=quantity+%s where name=%s"""
        cursor.execute(query,(stock,name))
        connection.commit()
        print("stock added successfully.")
    else:
        print("no such record found.") 
        connection.close()
        cursor.close()


#function to sell product
def sell_product():
    connection=create_connection()
    cursor=connection.cursor()
    name=input("enter product name:")
    cursor.execute("select quantity from products where name=%s",(name,))
    product=cursor.fetchone()
    if product:
        sold_quantity=int(input("enter quatity sold:"))
        if sold_quantity <=product[0]:
            cursor.execute("update products set quantity=quantity-%s where name=%s",(sold_quantity,name))
            connection.commit()
            print("sold quantity reduced successfully.")
        else:
            print("insufficient stock.")  
    else:
        print("no such record found.")          
    cursor.close()
    connection.close()


#function to view product
def view_product():
    connection=create_connection()
    cursor=connection.cursor()
    query="select*from products"
    cursor.execute(query)
    products=cursor.fetchall()
    if products:
        for product in products:
            print(product)
    else:
        print("no record found.")        

    cursor.close()
    connection.close()    

#function to find low stock products
def low_stock():
    connection=create_connection()
    cursor=connection.cursor()
    query="select*from products where quantity<20"
    cursor.execute(query)
    products=cursor.fetchall()
    if products:
        for product in products:
            print(product)
    else:
        print("no low stock exist.") 


while True:
    print("\n======== PRODUCT INVENTORY SYSTEM =========")
    print("1.add product")
    print("2.update price")
    print("3.add stock")  
    print("4.sell product")
    print("5.view product") 
    print("6.low stock product")
    print("7.exit")
    print("============================================")
    choice=input("enter your choice:")
    if choice=="1":
        add_product()
    elif choice=="2":
        update_product()
    elif choice=="3":
        add_stock()
    elif choice=="4":
        sell_product()
    elif choice=="5":
        view_product()
    elif choice=="6":
        low_stock()
    elif choice=="7":    
        print("exit.")
        break
    else:
        print("invalid choice.")            

                          
                         
        


                                  


          




