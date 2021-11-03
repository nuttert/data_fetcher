import json

class Crib:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def __str__(self):
        dict_res = {
            "name": str(self.name),
            "price": str(self.price),
        }
        return json.dumps(dict_res)

    def get_dict(self):
        dict_res = {
            "name": "'{}'".format(self.name),
            "price": self.price,
        }
        return dict_res