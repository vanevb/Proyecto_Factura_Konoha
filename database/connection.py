#!/usr/bin/env python3
"""
DAO model
"""

import mysql.connector
from mysql.connector import Error


class DAO():
    """ Connection class """

    def __init__(self):
        """ Create connection """
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='root',
                db='billing'
            )
        except Error as e:
            print(f"An error occurred while connecting to mysql: {e}")

    def get_clients(self):
        """ Get all clientes """
        if self.connection.is_connected():
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * from client")
                res = cursor.fetchall()
                return res
            except Error as e:
                print(f"An error occurred while retrieve data: {e}")
