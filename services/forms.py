#!/usr/bin/env python3
"""
Forms
"""


def capture_client_data(flag):
    """ Capture new client data """
    print("=> Create new client: \n" if flag == 0 else "=> Update client: \n")
    name = str(input("Name: "))
    cc = str(input("Cc: "))
    address = str(input("Address: "))
    phone = str(input("Phone: "))
    email = str(input("Email: "))
    return [name, cc, address, phone, email]


def capture_product_data(flag):
    """ Capture new product data """
    print("=> Create new product: \n" if flag ==
          0 else "=> Update product: \n")
    name_product = str(input("Product name : "))
    unit_value = int(input("Unit Value: "))
    ref = int(input("Ref: "))
    return [name_product, unit_value, ref]
