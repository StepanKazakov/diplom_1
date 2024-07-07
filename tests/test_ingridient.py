import pytest
from praktikum.database import Database


class TestIngredient:
    def setup_method(self):
        self.database = Database()
        self.ingredients = self.database.available_ingredients()

    @pytest.mark.parametrize("ingredient_index, expected_name", [
        (0, "hot sauce"),
        (1, "sour cream"),
        (2, "chili sauce"),
        (3, "cutlet"),
        (4, "dinosaur"),
        (5, "sausage")
    ])
    def test_ingredient_get_name(self, ingredient_index, expected_name):
        assert self.ingredients[ingredient_index].get_name() == expected_name

    @pytest.mark.parametrize("ingredient_index, expected_price", [
        (0, 100),
        (1, 200),
        (2, 300),
        (3, 100),
        (4, 200),
        (5, 300)
    ])
    def test_ingredient_get_price(self, ingredient_index, expected_price):
        assert self.ingredients[ingredient_index].get_price() == expected_price

    @pytest.mark.parametrize("ingredient_index, expected_type", [
        (0, "SAUCE"),
        (1, "SAUCE"),
        (2, "SAUCE"),
        (3, "FILLING"),
        (4, "FILLING"),
        (5, "FILLING")
    ])
    def test_ingredient_get_type(self, ingredient_index, expected_type):
        assert self.ingredients[ingredient_index].get_type() == expected_type
