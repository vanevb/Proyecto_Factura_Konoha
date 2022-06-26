#!/usr/bin/env python3
"""
Product model
"""


class Product():
    """ Product class """

    def __init__(self, name_product: str, price: int, quantity: int, ref: int):
        self.name_product = name_product
        self.price = price
        self.quantity = quantity
        self.ref = ref
