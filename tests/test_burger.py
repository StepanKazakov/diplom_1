from praktikum.burger import Burger
from praktikum.database import Database


class TestBurger:
    def setup_method(self):
        self.burger = Burger()
        self.database = Database()

    def test_set_buns(self):
        buns = self.database.available_buns()
        self.burger.set_buns(buns[0])
        assert self.burger.bun == buns[0]

    def test_add_ingredient(self):
        ingredients = self.database.available_ingredients()
        self.burger.add_ingredient(ingredients[1])
        self.burger.add_ingredient(ingredients[3])
        self.burger.add_ingredient(ingredients[2])
        assert self.burger.ingredients == [ingredients[1], ingredients[3], ingredients[2]]

    def test_remove_ingredient(self):
        ingredients = self.database.available_ingredients()
        self.burger.add_ingredient(ingredients[4])
        self.burger.add_ingredient(ingredients[3])
        self.burger.add_ingredient(ingredients[2])
        self.burger.remove_ingredient(1)
        assert ingredients[3] not in self.burger.ingredients

    def test_move_ingredient(self):
        ingredients = self.database.available_ingredients()
        self.burger.add_ingredient(ingredients[0])
        self.burger.add_ingredient(ingredients[2])
        self.burger.add_ingredient(ingredients[5])
        self.burger.move_ingredient(1, 2)
        assert self.burger.ingredients[1] == ingredients[5]
        assert self.burger.ingredients[2] == ingredients[2]

    def test_get_price(self):
        buns = self.database.available_buns()
        ingredients = self.database.available_ingredients()
        self.burger.set_buns(buns[1])
        self.burger.add_ingredient(ingredients[2])
        self.burger.add_ingredient(ingredients[4])
        self.burger.add_ingredient(ingredients[0])
        assert self.burger.get_price() == 1000

    def test_get_receipt(self):
        buns = self.database.available_buns()
        ingredients = self.database.available_ingredients()
        self.burger.set_buns(buns[2])
        self.burger.add_ingredient(ingredients[3])
        self.burger.add_ingredient(ingredients[1])
        expected_receipt = (
            "(==== red bun ====)\n"
            "= filling cutlet =\n"
            "= sauce sour cream =\n"
            "(==== red bun ====)\n"
            "\n"
            "Price: 900"
        )
        assert self.burger.get_receipt() == expected_receipt
