from django.db import models    

class Product:
    products = []

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def save(self):
        Product.products.append(self)

    @classmethod
    def all(cls):
        return cls.products

    @classmethod
    def get(cls, name):
        for product in cls.products:
            if product.name == name:
                return product
        return None
