import pytest
from bun import Bun
from ingredient import Ingredient

@pytest.fixture
def mock_bun():
    return Bun("Sesame", 1.5)

@pytest.fixture
def mock_ingredient():
    return Ingredient("Lettuce", 0.5)