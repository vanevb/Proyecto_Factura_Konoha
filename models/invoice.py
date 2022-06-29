#!/usr/bin/env python3
"""
Invoce model
"""


class Invoice():
    """ Invoice class """

    def __init__(self, client_id: int, product_id: int, quantity: int, cost: int):
        self.client_id = client_id
        self.product_id = product_id
        self.quantity = quantity
        self.cost = cost
