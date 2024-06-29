import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def mock_bun():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_price.return_value = 1.5
    mock_bun.get_name.return_value = "Sesame Bun"
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_price.return_value = 0.5
    mock_ingredient.get_name.return_value = "Lettuce"
    mock_ingredient.get_type.return_value = "FILLING"
    return mock_ingredient


@pytest.fixture
def mock_burger(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger


class TestBurger:
    def test_set_buns(self, mock_burger, mock_bun):
        mock_burger.set_buns(mock_bun)
        assert mock_burger.bun == mock_bun

    def test_add_ingredient(self, mock_burger, mock_ingredient):
        mock_burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in mock_burger.ingredients

    def test_remove_ingredient(self, mock_burger, mock_ingredient):
        mock_burger.add_ingredient(mock_ingredient)
        mock_burger.remove_ingredient(0)
        assert mock_ingredient not in mock_burger.ingredients

    def test_move_ingredient(self, mock_burger, mock_ingredient):
        another_mock_ingredient = Mock(spec=Ingredient)
        mock_burger.add_ingredient(mock_ingredient)
        mock_burger.add_ingredient(another_mock_ingredient)
        mock_burger.move_ingredient(0, 1)
        assert mock_burger.ingredients[1] == mock_ingredient

    def test_get_price(self, mock_burger, mock_bun, mock_ingredient):
        mock_burger.set_buns(mock_bun)
        mock_burger.add_ingredient(mock_ingredient)
        assert mock_burger.get_price() == 3.5  # 1.5 * 2 (buns) + 0.5 (ingredient)

    def test_get_receipt(self, mock_burger, mock_bun, mock_ingredient):
        mock_burger.set_buns(mock_bun)
        mock_burger.add_ingredient(mock_ingredient)
        receipt = mock_burger.get_receipt()
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= filling Lettuce =\n"
            "(==== Sesame Bun ====)\n"
            "Price: 3.5"
        )
        assert receipt == expected_receipt
