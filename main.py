#!/usr/bin/env python3
"""
Main application
"""

from models.client import Client
from models.invoice import Invoice
from models.product import Product
from services.show_data import show_data_from_db_client, show_data_from_db_product
from services.forms import capture_client_data
from services.forms import capture_product_data
import os


def client_handler(option: int):
    """ Function that handles to user option """
    client = Client()
    flag = 0

    if option == 1:
        """ Get """
        try:
            get_clients = client.get_all_clients()
            if len(get_clients) > 0:
                show_data_from_db_client(get_clients)
            else:
                print("Clients not found")
        except Exception as e:
            print(e)
    elif option == 2:
        """ Create """
        flag = 0
        try:
            data = capture_client_data()
            client.create_new_client(
                data[0], data[1], data[2], data[3], data[4])
        except Exception as e:
            print(e)
    elif option == 3:
        """ Update """
        flag = 1
        try:
            get_clients = client.get_all_clients()
            if len(get_clients) > 0:
                show_data_from_db_client(get_clients)
                update_client = int(input("Enter id client to update: "))
                if update_client != "":
                    data = capture_client_data(flag)
                    client.update_client(
                        update_client, data[0], data[1], data[2], data[3], data[4])
                else:
                    print("Invalid client id")
            else:
                print("Clients not found")
        except Exception as e:
            print(e)
    elif option == 4:
        """ Delete """
        try:
            get_clients = client.get_all_clients()
            if len(get_clients) > 0:
                show_data_from_db_client(get_clients)
                delete_client = int(input("Enter client id to delete: "))
                if delete_client != "":
                    client.delete_client(delete_client)
                else:
                    print("Invalid client id")
            else:
                print("Clients not found")
        except Exception as e:
            print(e)


def client_menu():
    """Client menu function for invoice """
    run = True

    while run:
        try:
            option = int(input("""
            === Client Invoicing System ==

            1. Get all clients
            2. Create new client
            3. Update client information
            4. Delete client
            5. Back

            Your option: """))

            if option < 1 or option > 5:
                os.system("clear")
                print("Incorrect option, please try again.")
            elif option == 5:
                print("\n=> Back to main menu.")
                run = False
            else:
                os.system("clear")
                client_handler(option)
        except ValueError:
            os.system("clear")
            print("Option must be an integer")


def product_handler(option: int):
    """ Function that handles to user option """
    product = Product()
    flag = 0

    if option == 1:
        """ Get """
        try:
            get_product = product.get_all_product()
            if len(get_product) > 0:
                show_data_from_db_product(get_product)
            else:
                print("Products not found")
        except Exception as e:
            print(e)
    elif option == 2:
        """ Create """
        flag = 0
        try:
            data = capture_product_data(flag)
            product.create_new_product(
                data[0], data[1], data[2])
        except Exception as e:
            print(e)
    elif option == 3:
        """ Update """
        flag = 1
        try:
            get_product = product.get_all_product()
            if len(get_product) > 0:
                show_data_from_db_product(get_product)
                update_product = int(input("Enter id product to update: "))
                if update_product != "":
                    data = capture_product_data(flag)
                    product.update_product(
                        update_product, data[0], data[1], data[2])
                else:
                    print("Invalid product id")
            else:
                print("Product not found")
        except Exception as e:
            print(e)

    elif option == 4:
        """ Delete """
        try:
            get_product = product.get_all_product()
            if len(get_product) > 0:
                show_data_from_db_product(get_product)
                delete_product = int(input("Enter id product to delete: "))
                if delete_product != "":
                    product.delete_product(delete_product)
                else:
                    print("Invalid product id")
            else:
                print("Product not found")
        except Exception as e:
            print(e)


def product_menu():
    product_run = True

    while product_run:
        try:
            option = int(input("""
            === Product Invoicing System ==

            1. Get all products
            2. Create new product
            3. Update product information
            4. Delete product
            5. Back

            Your option: """))

            if option < 1 or option > 5:
                os.system("clear")
                print("Incorrect option, please try again.")
            elif option == 5:
                print("\n=> Back to main menu.")
                product_run = False
            else:
                os.system("clear")
                product_handler(option)
        except ValueError:
            os.system("clear")
            print("Option must be an integer")


def main():
    main_run = True

    while main_run:
        try:
            option = int(input("""
            === Welcome to Invoicing System ==

            1. Client options
            2. Product options
            3. Invoicing
            4. Quit

            Your option: """))

            if option < 1 or option > 4:
                os.system("clear")
                print("Incorrect option, please try again.")
            elif option == 4:
                print("\n=> See you later.")
                main_run = False
            else:
                os.system("clear")
                if option == 1:
                    client_menu()
                elif option == 2:
                    product_menu()
                elif option == 3:
                    pass

        except ValueError:
            os.system("clear")
            print("Option must be an integer")


if __name__ == "__main__":
    main()
