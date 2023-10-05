
from lib.order import *
from lib.product_list import *

def test_add_item_to_order():
        menu = ProductList()
        menu.add_product("Cafe Latte", 3.50)

        order = Order(menu)
        order.add_item("Cafe Latte", 2)

        assert order.get_item_quantity("Cafe Latte") == 2
