import MySQLdb as sql


def connection():
    """
    Function to connect to server
    """
    try:
        connect = sql.connect(
            db='python_mysql',
            host='localhost',
            user='leo',
            passwd='treino')
        return connect # Connection to the database
    except sql.Error as e: 
        print(f'Connection error: {e}')


def disconnection(connect):
    """
    Function to disconnect from server
    """
    if connect: # Check if there is a connection
        connect.close()


def list_products():
    """
    Function to list products
    """
    connect = connection() # Create connection
    cursor = connect.cursor() # Resource to script in SQL
    cursor.execute('SELECT * FROM PRODUTOS') # SQL 
    products = cursor.fetchall() # Take select data and pass to a list

    if len(products) > 0: # If there are produtcs
        print('Listing products')
        print('----------------')
        for product in products:
            print(f'ID: {product[0]}')
            print(f'Product: {product[1]}')
            print(f'Price: {product[2]}')
            print(f'Stash: {product[3]}')
    else:
        print('There are no products')
    disconnection(connect)


def insert_product():
    """
    Function to insert a product
    """
    connect = connection() # Create connection
    cursor = connect.cursor() # Resource to script in SQL

    name = input('Product name to insert: ') # Name
    price = float(input('Product price: ')) # Price
    stash = int(input('Product stash: ')) # Stash

    cursor.execute(f"INSERT INTO PRODUTOS (nome, preco, estoque) VALUES ('{name}', {price}, {stash})") # SQL
    connect.commit() # Commit

    if cursor.rowcount == 1: # Check if the insert worked
        print(f'Product  {name} inserted')
    else:
        print('Error inserting product')
    
    disconnection(connect)


def update_product():
    """
    Function to update a product
    """
    connect = connection() # Create connection
    cursor = connect.cursor() # Resource to script in SQL
    
    code = int(input('Provide product code to update: ')) # product to be updated

    name = input('Provide product new/updated name: ') # New name
    price = float(input('Provide product new/updated price: ')) # New price
    stash = int(input('Provide new/updated stash: ')) # New stash

    cursor.execute(F"UPDATE PRODUTOS SET nome='{name}', preco={price}, estoque={stash} WHERE id={code}")
    connect.commit()

    if cursor.rowcount == 1: # Check if the insert worked
        print(f'Product {code} updated')
    else:
        print('Product not updated')

    disconnection(connect)


def delete_product():
    """
    Function to delete product
    """
    connect = connection() # Create connection
    cursor = connect.cursor() # Resource to script in SQL
    
    code = int(input('Provide product code to delete: ')) # product to be deleted
    cursor.execute(f'DELETE FROM PRODUTOS WHERE id={code}')
    connect.commit()

    if cursor.rowcount == 1:
        print('Product deleted')
    else:
        print('Product not deleted')
    disconnection(connect)


def menu():
    """
    Function to generate main menu
    """
    print('=========Product management==============')
    print('Selection one option: ')
    print('1 - List products.')
    print('2 - Insert product.')
    print('3 - Update product.')
    print('4 - Delete product.')
    option = int(input())
    if option in [1, 2, 3, 4]:
        if option == 1:
            list_products()
        elif option == 2:
            insert_product()
        elif option == 3:
            update_product()
        elif option == 4:
            delete_product()
        else:
            print('Invalid option')
    else:
        print('Invalid option')
