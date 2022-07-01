#!/usr/bin/env python3
"""
Main application
"""

import os
from services.client_menu import client_menu
from services.product_menu import product_menu
from services.invoice_menu import invoice_menu


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
                    invoice_menu()

        except ValueError:
            os.system("clear")
            print("Option must be an integer")


if __name__ == "__main__":
    main()
