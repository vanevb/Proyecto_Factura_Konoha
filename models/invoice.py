#!/usr/bin/env python3
"""
Invoce model
"""

from datetime import datetime


class Invoice():
    """ Invoice class """

    def __init__(self, name_client: str, nit_cc: int, product: str, quantity: int, cost: float, iva: float, date: datetime):
        self.name_client = name_client
        self.nit_cc = nit_cc
        self.product = product
        self.quantity = quantity
        self.cost = cost
        self.iva = iva
        self.date = date
