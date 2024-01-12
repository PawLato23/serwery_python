#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional


class Product:
    def __init__(self, name: str, price: float):
        if not name.isalnum():  #sprawdzenie czy na pewno tylko litery i cyfry
            raise ValueError
        if not (isinstance(price, (int, float)) and price > 0):
            raise ValueError
        #sprawdzenie, czy na pewno foramat xxx000
        nnum = nchr = 0
        for it in name:
            if it.isdigit():
                nnum += 1
            elif nnum == 0: #sprawdza czy na pewno najpierw sa literki, potem cyfry
                nchr += 1
            else:
                raise ValueError     
        if nnum == 0 or nchr == 0:  #sprawdza czy napewno jest przynajmniej jedna cyfra i literka
            raise ValueError
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        return False

    def __hash__(self):
        return hash((self.name, self.price))
    
    def __str__(self):
        return f"{self.name} : {self.price}"

    def get_name(self): 
        return self.name
    def get_price(self):
        return self.price
    def get(self):
        return (self.name, self.price)

class TooManyProductsFoundError(Exception):
    pass


class ListServer:
    pass


class MapServer:
    pass


class Client:

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()

'''        
p1 = Product("aaa1321", 12)
p2 = Product("aab2", 13)
p3 = Product("aaa1321", 12)
'''