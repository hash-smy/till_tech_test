from lib.product_list import *
import pytest


def test_get_product_price():
        menu = ProductList()
        menu.add_product("Cafe Latte", 3.50)
        assert menu.get_product_price("Cafe Latte") == 3.50

def test_product_not_found():
        menu = ProductList()
        with pytest.raises(Exception):
                menu.get_product_price("Non-existent Product")
