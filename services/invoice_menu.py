#!/usr/bin/env python3
"""
Invoice menu
"""

import os
from models.invoice import Invoice
from services.forms import capture_invoice_data
from services.show_data import show_data_from_db_invoice
from services.client_menu import client_handler
from services.product_menu import product_handler


def invoice_handler(option: int):
    """ Function that handles invoice options """
    invoice = Invoice()
    flag = 0

    if option == 1:
        """ Get """
        try:
            get_invoices = invoice.get_all_invoices()
            if len(get_invoices) > 0:
                show_data_from_db_invoice(get_invoices)
            else:
                print("Invoices not found")
        except Exception as e:
            print(e)
    elif option == 2:
        """ Create """
        try:
            client_handler(1)
            print("")
            product_handler(1)
            data = capture_invoice_data()
            invoice.create_new_invoice(
                data[0], data[1], data[2], total_value=0)
        except Exception as e:
            print(e)
    elif option == 3:
        """ Delete """
        try:
            get_invoices = invoice.get_all_invoices()
            if len(get_invoices) > 0:
                show_data_from_db_invoice(get_invoices)
                delete_invoice = int(input("Enter invoice id to delete: "))
                if delete_invoice != "":
                    invoice.delete_invoice(delete_invoice)
                else:
                    print("Invalid invoice id")
            else:
                print("Invoices not found")
        except Exception as e:
            print(e)


def invoice_menu():
    """Invoice menu function """
    run = True

    while run:
        try:
            option = int(input("""
            === Client Invoicing System ==

            1. Get all invoices
            2. Create new invoice
            3. Delete invoice
            4. Back

            Your option: """))

            if option < 1 or option > 4:
                os.system("clear")
                print("Incorrect option, please try again.")
            elif option == 4:
                print("\n=> Back to main menu.")
                run = False
            else:
                os.system("clear")
                invoice_handler(option)
        except ValueError:
            os.system("clear")
            print("Option must be an integer")
