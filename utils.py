import redis


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
    print('Listing products...')


def insert_products():
    """
    Function to insert a product
    """
    print('Inserting a product...')


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
