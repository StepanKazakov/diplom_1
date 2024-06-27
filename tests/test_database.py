import pytest
from database import Database
from burger import Burger
from bun import Bun
from ingredient import Ingredient

@pytest.fixture
def mock_burger():
    bun = Bun("Sesame", 1.5)
    burger = Burger(bun)
    burger.add_ingredient(Ingredient("Lettuce", 0.5))
    return burger

def test_database_initialization():
    db = Database()
    assert db.data == []

def test_database_add_burger(mock_burger):
    db = Database()
    db.add_burger(mock_burger)
    assert mock_burger in db.data

def test_database_get_all_burgers(mock_burger):
    db = Database()
    db.add_burger(mock_burger)
    assert db.get_all_burgers() == [mock_burger]