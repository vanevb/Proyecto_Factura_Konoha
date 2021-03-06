#!/usr/bin/env python3
"""
Product model
"""

from mysql.connector import Error
from database.connection import DAO


class Product (DAO):
    """ Product class """

    def __init__(self):
        """ Inherit connection """
        super().__init__()

    def get_all_product(self):
        """ Get all product"""
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * from product")
                products_result = cursor.fetchall()
                return products_result
            except Error as e:
                print(f"An error occurred while retrieve data: {e}")

    def create_new_product(self, name_product: str, unit_value: int, ref: int):
        """ Create new product """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = f"INSERT INTO product (name_product, unit_value, ref) VALUES ('{name_product}', '{unit_value}', '{ref}')"
                cursor.execute(sql)
                self.connection.commit()
                print("\n=> Product created successfully")
            except Error as e:
                print(f"An error occurred while creating the product: {e}")

    def update_product(self, update_product: int, name_product: str, unit_value: int, ref: int):
        """ Update product """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = f"UPDATE product SET name_product = '{name_product}', unit_value = '{unit_value}', ref = '{ref}' WHERE id = {update_product}"
                cursor.execute(sql)
                self.connection.commit()
                print("\n=> Product update successfully")
            except Error as e:
                print(f"An error occurred while update the product: {e}")

    def delete_product(self, id: int):
        """ Delete product by id """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = f"DELETE FROM product WHERE id = '{id}'"
                cursor.execute(sql)
                self.connection.commit()
                print("\n=> Product deleted successfully")
            except Error as e:
                print(f"An error occurred while deleting the product: {e}")
