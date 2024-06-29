from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from praktikum.database import Database


class TestIngredient:
    def test_ingredient_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 0.5)
        assert ingredient.get_name() == "Ketchup"

    def test_ingredient_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 0.5)
        assert ingredient.get_price() == 0.5

    def test_ingredient_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Ketchup", 0.5)
        assert ingredient.get_type() == 'FILLING'
