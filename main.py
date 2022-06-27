#!/usr/bin/env python3
"""
Main application
"""

from models.client import Client
from models.invoice import Invoice
from models.product import Product
from services.show_data import show_data_from_db
from services.forms import capture_client_data
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
                os.system("clear")
                client_handler(option)
        except ValueError:
            os.system("clear")
            print("Option must be an integer")


def client_handler(option):
    """ Function that handles to user option """
    client = Client()

    if option == 1:
        """ Get """
        try:
            get_clients = client.get_all_clients()
            if len(get_clients) > 0:
                show_data_from_db(get_clients)
            else:
                print("Clients not found")
        except Exception as e:
            print(e)
    elif option == 2:
        """ Create """
        try:
            data = capture_client_data()
            client.create_new_client(
                data[0], data[1], data[2], data[3], data[4])
        except Exception as e:
            print(e)
    elif option == 3:
        print("Update")
    elif option == 4:
        """ Delete """
        try:
            get_clients = client.get_all_clients()
            if len(get_clients) > 0:
                show_data_from_db(get_clients)
                delete_client = int(input("Enter client id to delete: "))
                if delete_client != "":
                    client.delete_client(delete_client)
                else:
                    print("Invalid client id")
            else:
                print("Clients not found")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
