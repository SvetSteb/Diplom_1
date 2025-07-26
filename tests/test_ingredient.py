import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from data import *


class TestIngredient:

    @pytest.fixture(autouse=True)
    def ingredient(self):
        test_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_FILLING,
                                     INGREDIENT_PRICE_FILLING)
        return test_ingredient

    # Тестирование метода инициализации
    @pytest.mark.parametrize('name, price, type',[(INGREDIENT_NAME_FILLING, INGREDIENT_PRICE_FILLING, INGREDIENT_TYPE_FILLING),
                                                  (INGREDIENT_NAME_SAUSE, INGREDIENT_PRICE_SAUSE, INGREDIENT_TYPE_SAUCE)])
    def test_init_ingredient_is_initialized(self, name, price, type):
        ingredient = Ingredient(type, name, price)
        expected_result = {'name': name,
                           'price': price, 
                           'type': type}
        assert ingredient.__dict__ == expected_result

    # Тест метода get_price
    def test_get_price_return_current_ingredient_price(self, ingredient):
        assert ingredient.get_price() == INGREDIENT_PRICE_FILLING

    # Тест метода get_name
    def test_get_name_return_current_ingredient_name(self, ingredient):
        assert ingredient.get_name() == INGREDIENT_NAME_FILLING

    # Тест метода get_type
    def test_get_type_return_filling(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING