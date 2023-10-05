
from lib.order import *
from lib.product_list import *

def test_add_item_to_order():
        menu = ProductList()
        menu.add_product("Cafe Latte", 3.50)

        order = Order(menu)
        order.add_item("Cafe Latte", 2)

        assert order.get_item_quantity("Cafe Latte") == 2

def test_order_total():
        menu = ProductList()
        menu.add_product("Cafe Latte", 3.50)
        menu.add_product("Espresso", 2.00)

        order = Order(menu)
        order.add_item("Cafe Latte", 2)
        order.add_item("Espresso", 3)

        total = order.calculate_total()
        assert total == (3.50 * 2) + (2.00 * 3)


