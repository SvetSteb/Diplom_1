import pytest

from praktikum.bun import Bun
from data import *


class TestBun:

    # Тест метода __init__
    def test_init_class_object_is_initialized(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.__dict__ == {'name': BUN_NAME, 'price': BUN_PRICE}

    # Тест метода get_name
    @pytest.mark.parametrize('name', ['Bun', 'Булка', 'БУЛКА', 'бyл0-4k@'])
    def test_get_name_return_name(self, name):
        bun = Bun(name, 10)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [0, 0.0, 0.01, 1, 100.5])
    # Тест метода get_price
    def test_get_price_return_price(self, price):
        bun = Bun('Булочка', price)
        assert bun.get_price() == price
