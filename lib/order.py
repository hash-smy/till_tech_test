from lib.product_list import *
class Order:
    def __init__(self, product_list):
        self.items = {}
        self.product_list = product_list

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def get_item_quantity(self, name):
        return self.items.get(name, 0)

    def calculate_total(self):
        total = 0 
        for item , quantity in self.items.items():
            price = self.product_list.get_product_price(item)
            total += price * quantity
        return total