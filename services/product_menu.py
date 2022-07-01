#!/usr/bin/env python3
"""
Product menu
"""

import os
from models.product import Product
from services.show_data import show_data_from_db_product
from services.forms import capture_product_data


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
