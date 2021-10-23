import redis


def generate_id():
    try:
        connect = connection()

        keys = connect.get('key')

        if keys:
            keys = connect.incr('key')
            return keys
        else:
            connect.set('key', 1)
            return 1
    except redis.exceptions.ConnectionError as e:
        print(f'It was not possible to generate the key: {e}')


def connection():
    """
    Function to connect to server
    """
    connect = redis.Redis(host='localhost', port=6379)

    print('Connection to server...')

    return connect


def disconnection(connect):
    """
    Function to disconnect from server
    """
    connect.connection_pool.disconnect()

    print('Disconnecting from server...')


def list_products():
    """
    Function to list products
    """
    connect = connection()

    try:
        data = connect.keys(pattern='produtos:*')
        if len(data) > 0:
            print('Listing products...')
            print('-------------------')
            for keys in data:
                product = connect.hgetall(keys)
                print(f"ID: {str(keys, 'utf-8', 'ignore')}")
                print(f"Product: {str(product[b'name'], 'utf-8', 'ignore')}")
                print(f"Price: {str(product[b'price'], 'utf-8', 'ignore')}")
                print(f"Stash: {str(product[b'stash'], 'utf-8', 'ignore')}")
                print('-------------------')
        else:
            print('There are no products registred')
    except redis.exceptions.ConnectionError as e:
        print(f'It was not possible to list the products: {e}')

    disconnection(connect)


def insert_products():
    """
    Function to insert a product
    """
    connect = connection()

    name = input('Product name to insert: ')
    price = float(input('Product price: '))
    stash = int(input('Product stash: '))

    product = {'Name': name, 'Price': price, 'Stash': stash}
    keys = f'product:{generate_id()}'

    try:
        answer = connect.hmset(keys, product)

        if answer:
            print(f'The product {name} was successfully inserted.')
        else:
            print(f'It was not possible to insert the product')
    except redis.exceptions.ConnectionError as e:
        print(f'It was not possible to insert the product: {e}')

    disconnection(connect)


def update_product():
    """
    Function to update a product
    """
    print('Updating product...')


def delete_product():
    """
    Function to delete product
    """
    print('Deleting product...')


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
            insert_products()
        elif option == 3:
            update_product()
        elif option == 4:
            delete_product()
        else:
            print('Invalid option')
    else:
        print('Invalid option')
