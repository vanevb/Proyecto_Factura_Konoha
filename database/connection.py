#!/usr/bin/env python3
"""
DAO model
"""

import mysql.connector
from mysql.connector import Error

# sudo /etc/init.d/mysql start
# sudo service --status-all
# sudo mysql -uroot -p
# mysqldump -u root -p invoice > invoice.sql


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
                db='invoice'
            )
        except Error as e:
            print(f"An error occurred while connecting to mysql: {e}")
