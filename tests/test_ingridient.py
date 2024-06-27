from ingredient import Ingredient

def test_ingredient_initialization():
    ingredient = Ingredient("Tomato", 0.3)
    assert ingredient.name == "Tomato"
    assert ingredient.price == 0.3

def test_ingredient_price():
    ingredient = Ingredient("Cheese", 0.7)
    assert ingredient.get_price() == 0.7

def test_ingredient_str():
    ingredient = Ingredient("Onion", 0.2)
    assert str(ingredient) == "Onion: $0.2"