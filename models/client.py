#!/usr/bin/env python3
"""
Client model
"""

from mysql.connector import Error
from database.connection import DAO


class Client(DAO):
    """ Client class """

    def __init__(self):
        """ Inherit connection """
        super().__init__()

    def get_all_clients(self):
        """ Get all clientes """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * from client")
                res = cursor.fetchall()
                return res
            except Error as e:
                print(f"An error occurred while retrieve data: {e}")

    def create_new_client(self, name_client, nit_cc, address, phone, email):
        """ Create new client """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = f"INSERT INTO client (name, nit, address, phone, email) VALUES ('{name_client}', '{nit_cc}', '{address}', '{phone}', '{email}')"
                cursor.execute(sql)
                self.connection.commit()
                print("\n=> Client created successfully")
            except Error as e:
                print(f"An error occurred while creating the client: {e}")
