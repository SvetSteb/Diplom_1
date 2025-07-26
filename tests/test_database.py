import pytest

from praktikum.database import Database

class TestDatabase:

    @pytest.fixture(autouse=True)
    def db(self):
        db = Database()
        return db


    def test_available_buns_return_list_len_three(self, db):
        assert len(db.available_buns()) == 3

    def test_available_ingredients_return_list_len_six(self, db):
        assert len(db.available_ingredients()) == 6

    def test_available_buns_add_new_bun_return_list_len_four(self, db, bun_mock):
        db.buns.append(bun_mock)
        assert len(db.available_buns()) == 4

    def test_available_ingredients_add_new_return_list_len_seven(self, db, ingredient_mock_filling):
        db.ingredients.append(ingredient_mock_filling)
        assert len(db.available_ingredients()) == 7