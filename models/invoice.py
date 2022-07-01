#!/usr/bin/env python3
"""
Invoce model
"""

from mysql.connector import Error
from database.connection import DAO


class Invoice(DAO):
    """ Invoice class """

    def __init__(self):
        """ Inherit connection """
        super().__init__()

    def get_all_invoices(self):
        """ Get all invoicing """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT invoice.id, client.nit, client.name, product.name_product, product.unit_value, invoice.quantity, product.unit_value * invoice.quantity AS total_value FROM invoice JOIN client ON client.id = invoice.client_id JOIN product ON product.id = invoice.product_id;")
                invoice_result = cursor.fetchall()
                return invoice_result
            except Error as e:
                print(f"An error occurred while retrieve data: {e}")

    def get_invoice(self, id: int):
        """ Get invoice by id """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = f"SELECT FROM invoice WHERE id = '{id}'"
                cursor.execute(sql)
                invoice_result = cursor.fetchall()
                return invoice_result
            except Error as e:
                print(f"An error occurred while retrieve data: {e}")

    def create_new_invoice(self, client_id: int, product_id: int, quantity: int, total_value: int):
        """ Create new invoice """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = f"INSERT INTO invoice (client_id, product_id, quantity, total_value) VALUES ('{client_id}', '{product_id}', '{quantity}', {total_value})"
                cursor.execute(sql)
                self.connection.commit()
                print("\n=> Invoice created successfully")
            except Error as e:
                print(f"An error occurred while creating the invoice: {e}")

    def delete_invoice(self, id: int):
        """ Delete invoice by id """
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = f"DELETE FROM invoice WHERE id = '{id}'"
                cursor.execute(sql)
                self.connection.commit()
                print("\n=> Invoice deleted successfully")
            except Error as e:
                print(f"An error occurred while deleting the invoice: {e}")
