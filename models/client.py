#!/usr/bin/env python3
"""
Client model
"""


class Client:
    """ Client class """

    def __init__(self, name_client: str, nit_cc: int, adress: str, phone: int, email: str):
        self.name_client = name_client
        self.nit_cc = nit_cc
        self.adress = adress
        self.phone = phone
        self.email = email
