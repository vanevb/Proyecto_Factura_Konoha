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

    # def __init__(self, name_client: str, nit_cc: int, address: str, phone: int, email: str):
    #     super().__init__()
    #     self.name_client = name_client
    #     self.nit_cc = nit_cc
    #     self.address = address
    #     self.phone = phone
    #     self.email = email

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
