import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient

@pytest.fixture
def mock_bun():
    return Bun("Sesame", 1.5)

@pytest.fixture
def mock_ingredient():
    return Ingredient("Lettuce", 0.5)

def test_burger_initialization(mock_bun):
    burger = Burger(mock_bun)
    assert burger.bun == mock_bun
    assert burger.ingredients == []

def test_burger_add_ingredient(mock_bun, mock_ingredient):
    burger = Burger(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients

def test_burger_price(mock_bun, mock_ingredient):
    burger = Burger(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert burger.get_price() == 2.0  # 1.5 (bun) + 0.5 (ingredient)

def test_burger_str(mock_bun, mock_ingredient):
    burger = Burger(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert str(burger) == "Burger with Sesame bun: 1 ingredients"