from praktikum.database import Database


class TestDatabase:
    def setup_method(self):
        self.database = Database()

    def test_available_buns(self):
        buns = self.database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"
