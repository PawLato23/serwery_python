#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List
from abc import ABC


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


class ServerError(Exception):
    pass


class TooManyProductsFoundError(ServerError): #raise TooManyProductsFoundError("o 2 za duzo")
    pass


class Server(ABC):
    n_max_returned_entries = 5

    def __init__(self, list_of_products: List):
        if type(list_of_products) != list:
            raise TypeError

    def __str__(self):
        raise NotImplementedError("not having __str__ method")

    def entries(self, n_letters: int) -> List:
        raise NotImplementedError("not having this method")

    def check_entry(self, product: Product) -> bool:
        pass

    def get_entries(self, n_letters: int) -> List:
        entries = self.entries(n_letters)
        if len(entries) > self.n_max_returned_entries:
            raise TooManyProductsFoundError
        else:
            return entries


class ListServer(Server):
    def __init__(self, list_of_products: List):
        super().__init__(list_of_products)
        self.products = list_of_products.copy()

    def __str__(self):
        return str(self.products)

    def entries(self, n_letters: int) -> List:
        result_list = []
        for prod in self.products:
            if self.check_entry(prod):
                result_list.append(prod)
        return result_list


class MapServer(Server):
    def __init__(self, list_of_products: List):
        super().__init__(list_of_products)
        self.products = dict()
        for it in list_of_products:
            self.products[it.get_name()] = it

    def __str__(self):
        return str(self.products)

    def entries(self, n_letters: int) -> List:
        result_list = []
        for prod in self.products.values():
            if self.check_entry(prod):
                result_list.append(prod)
        return result_list


class Client:
    def __init__(self, server: Server):
        #self.client_server = server
        pass       
    
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
