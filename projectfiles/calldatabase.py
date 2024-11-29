import mysql.connector


def connect_db():
    return mysql.connector.connect(
        user='root', password='Sreyporyou32', host='127.0.0.1', database='grocerystore'
    )

def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM user_info WHERE user_name = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return bool(result)  # Return True if a match is found

    

def instock_product():
    cnx = connect_db()
    cursor = cnx.cursor()
    query = (
        "SELECT products.product_id, products.product_name, categories.category_name, products.Price_per_Unit, products.unit_name, products.Quantity "
        "FROM products "
        "INNER JOIN categories ON products.category_id = categories.category_id "
        "ORDER BY products.product_id ASC"
    )

    cursor.execute(query)

    response = []
    for (product_id, product_name,  category, Price_per_unit, Quantity, unit_name) in cursor:
        response.append((product_id, product_name, category, Price_per_unit, Quantity, unit_name))
    
    cursor.close()
    cnx.close()
    return response


def all_categories():
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    
    categories = cursor.fetchall()  
    cursor.close()
    cnx.close()
    return categories



def products_by_category(category_id):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = (
        "SELECT products.product_id, products.product_name, categories.category_name, products.price_per_unit, products.unit_name, products.Quantity "
        "FROM products "
        "INNER JOIN categories ON products.category_id = categories.category_id "
        "WHERE products.category_id = %s "
        "ORDER BY products.product_id ASC;"
    )

    cursor.execute(query, (category_id,))
    
    products = cursor.fetchall()  
    cursor.close()
    cnx.close()
    return products




def insert_new_product(product_name, unit_name, category_id, price_per_unit, Quantity):
    try:
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute("SELECT 1 FROM products WHERE product_name = %s", (product_name,))
        if cursor.fetchone():
            return "Error: Product already exists in the database."
        else:
            query = "INSERT INTO products (product_name, unit_name, category_id, Price_per_unit, Quantity) VALUES (%s, %s, %s, %s, %s)"
            data = (product_name, unit_name, category_id, price_per_unit, Quantity)
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
    except mysql.connector.Error as err:
        return f"Error: {err}"


def delete_product(product_id):
    try:
        cnx = connect_db()
        cursor = cnx.cursor()
        query = "DELETE FROM products WHERE product_id = %s"
        cursor.execute(query, (product_id,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    except mysql.connector.Error as err:
        return f"Error: Invalid ID "

def update_stock(new_quatity, product_id):
    try:
        cnx = connect_db()
        cursor = cnx.cursor()
        query = "UPDATE products SET quantity = %s WHERE product_id = %s"
        cursor.execute(query, (new_quatity, product_id))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    except mysql.connector.Error as err:
        return f"Error: Can't update stock"




