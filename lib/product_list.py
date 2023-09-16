
# class ProductList:
#     def __init__(self, pricelist):
#             self.products = self.load_pricelist(pricelist)

    

#     def get_price(self,name):
#         if name in self.products:
#             return self.products[name]
#         # else:
#         #     raise Exception("Item not found")

#     def add_item(self,name, price):
#         self.products[name] = price


class ProductList:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price

    def get_product_price(self, name):
        if name in self.products:
            return self.products[name]
        else:
            raise Exception("Product not found in the catalog.")