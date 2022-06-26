#!/usr/bin/env python3
"""
Main application
"""

from models.client import Client
from models.invoice import Invoice
from models.product import Product
from database.connection import DAO
import os


def main():
    """ Main function for invoice """
    run = True

    while run:
        try:
            option = int(input("""
=== Welcome to Invoicing System ==

1. Get all clients
2. Create new client
3. Update client information
4. Delete client
5. Quit

Your option: """))

            if option < 1 or option > 5:
                os.system("clear")
                print("Incorrect option, please try again.")
            elif option == 5:
                print("\n=> See you later.")
                run = False
            else:
                option_handler(option)
        except ValueError:
            os.system("clear")
            print("Option must be an integer")


def option_handler(option):
    """ Function that handles to user option """
    dao = DAO()

    if option == 1:
        try:
            get_clients = dao.get_clients()
            if len(get_clients) > 0:
                print(get_clients)
            else:
                print("Clients not found")
        except Exception as e:
            print(e)
    elif option == 2:
        print("Create")
    elif option == 3:
        print("Update")
    elif option == 4:
        print("Delete")


if __name__ == "__main__":
    main()
