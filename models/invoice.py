#!/usr/bin/env python3
"""
Invoice model
"""

from datetime import datetime
from mysql.connector import Error
from database.connection import DAO
from client import Client

class Invoice(DAO):
    """ Invoice class """
    
    def __init__(self):
        """ Inherit connection """
        super().__init__()
        
    def create_new_invoice(self, name_client, nit_cc, product, quantity, cost, iva, date):
        self.name_client = name_client
        self.nit_cc = nit_cc
        self.product = product
        self.quantity = quantity
        self.cost = cost
        self.iva = iva
        self.date = date
    
