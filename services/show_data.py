#!/usr/bin/env python3
"""
Show data
"""


def show_data_from_db_client(get_clients):
    """ Return a pretty representation of client data """
    print("=> All clients: \n")
    for client in get_clients:
        print(
            f"ID:{client[0]} | Name: {client[1]} | Cc: {client[2]} | Address: {client[3]} | Phone: {client[4]} | Email: {client[5]}\n")


def show_data_from_db_product(get_product):
    """ Return a pretty representation of product data """
    for product in get_product:
        print(
            f"ID:{product[0]} | Name product: {product[1]} | Unit value: {product[2]} | Ref: {product[3]}\n")
