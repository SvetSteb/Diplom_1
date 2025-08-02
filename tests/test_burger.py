import pytest

from unittest.mock import Mock

from praktikum.burger import Burger
from data import *

class TestBurger:

    # фикстура для тестирования класса Burger
    @pytest.fixture(autouse=True)
    def burger(self):
        test_burger = Burger()
        return test_burger
    
    # Тестирование инициализации объекта класса Burger
    def test_init_object_is_initialized(self, burger):
        assert burger.__dict__ == {'bun': None, 'ingredients': []}

    # Тест метода set_buns 
    def test_set_buns_get_attribute_return_buns(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    # Тест метода add_ingredient
    def test_add_one_ingredient_get_list_return_one(self, burger, ingredient_mock_filling):
        burger.add_ingredient(ingredient_mock_filling)
        assert burger.ingredients == [ingredient_mock_filling]

    # Тест метода
    def test_remove_ingredient_add_than_remove_ingredient_return_empty_list(self, burger, ingredient_mock_sause):
        burger.add_ingredient(ingredient_mock_sause)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    # Тест метода move_ingredient
    def test_move_ingredient_add_two_ingredients_than_move_get_list_return_new_list(self, 
            burger, ingredient_mock_filling, ingredient_mock_sause):
        ingredient_1 = ingredient_mock_filling
        ingredient_2 = ingredient_mock_sause
        ingredient_3 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient_2, ingredient_3, ingredient_1]

    # Тест метода get_price
    def test_get_price_buns_and_two_ingridients_return_total(self, burger, bun_mock, ingredient_mock_sause, ingredient_mock_filling):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_filling)
        burger.add_ingredient(ingredient_mock_sause)
        expected_price = bun_mock.get_price() * 2 + ingredient_mock_filling.get_price() + ingredient_mock_sause.get_price()
        assert burger.get_price() == expected_price

    # Тест метода get_recept
    def test_get_recept_return_recept(self, burger, bun_mock, ingredient_mock_sause, ingredient_mock_filling):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_filling)
        burger.add_ingredient(ingredient_mock_sause)
        words = [bun_mock.get_name(),
                 ingredient_mock_filling.get_name(),
                 ingredient_mock_sause.get_name()]
        receipt = burger.get_receipt()
        assert all(word in receipt for word in words)

