import pytest

from unittest.mock import Mock

from data import *
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from praktikum.bun import Bun

# Фикстура для создания объекта класса для каждого теста
@pytest.fixture
def bun():
    test_bun = Bun(BUN_NAME, BUN_PRICE)
    return test_bun

@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_price.return_value = BUN_PRICE
    bun_mock.get_name.return_value = BUN_NAME
    return bun_mock

@pytest.fixture
def ingredient_mock_sause():
    ingredient_mock = Mock()
    ingredient_mock.get_price.return_value = INGREDIENT_PRICE_SAUSE
    ingredient_mock.get_name.return_value = INGREDIENT_NAME_SAUSE
    ingredient_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient_mock

@pytest.fixture
def ingredient_mock_filling():
    ingredient_mock = Mock()
    ingredient_mock.get_price.return_value = INGREDIENT_PRICE_FILLING
    ingredient_mock.get_name.return_value = INGREDIENT_NAME_FILLING
    ingredient_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient_mock
