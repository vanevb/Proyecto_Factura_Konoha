#!/usr/bin/env python3
"""
Forms
"""


def capture_client_data(flag):
    """ Capture new client data """
    print("\n=> Create new client: \n" if flag ==
          0 else "\n=> Update client: \n")
    name = str(input("Name: "))
    cc = str(input("Cc: "))
    address = str(input("Address: "))
    phone = str(input("Phone: "))
    email = str(input("Email: "))
    return [name, cc, address, phone, email]


def capture_product_data(flag):
    """ Capture new product data """
    print("\n=> Create new product: \n" if flag ==
          0 else "\n=> Update product: \n")
    name_product = str(input("Product name : "))
    unit_value = int(input("Unit Value: "))
    ref = int(input("Ref: "))
    return [name_product, unit_value, ref]


def capture_invoice_data():
    """ Capture new invoice data """
    print("\n=> Create new invoice: \n")
    client_id = int(input("Client ID : "))
    product_id = int(input("Product ID: "))
    quantity = int(input("Quantity: "))
    return [client_id, product_id, quantity]
