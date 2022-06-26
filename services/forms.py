#!/usr/bin/env python3
"""
Forms
"""


def capture_client_data():
    """ Capture new client data """
    print("=> Create new client: \n")
    name = str(input("Name: "))
    cc = str(input("Cc: "))
    address = str(input("Address: "))
    phone = str(input("Phone: "))
    email = str(input("Email: "))
    return [name, cc, address, phone, email]
