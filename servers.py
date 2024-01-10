#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional


class Product:

    def __eq__(self, other):
        return None

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError:
    pass


class ListServer:
    pass


class MapServer:
    pass


class Client:

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()