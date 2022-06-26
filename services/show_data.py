#!/usr/bin/env python3
"""
Show data
"""


def show_data_from_db(get_clients):
    """ Return a pretty representation of data """
    print("=> All clients: \n")
    for client in get_clients:
        print(
            f"ID:{client[0]} | Name: {client[1]} | Cc: {client[2]} | Address: {client[3]} | Phone: {client[4]} | Email: {client[5]}\n")
