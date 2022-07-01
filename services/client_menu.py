#!/usr/bin/env python3
"""
Client menu
"""

import os
from models.client import Client
from services.forms import capture_client_data
from services.show_data import show_data_from_db_client


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
            data = capture_client_data(flag)
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
