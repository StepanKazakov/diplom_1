import pytest
from praktikum.database import Database


class TestBun:
    def setup_method(self):
        self.database = Database()
        self.buns = self.database.available_buns()

    @pytest.mark.parametrize("bun_index, expected_name", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun")
    ])
    def test_bun_get_name(self, bun_index, expected_name):
        assert self.buns[bun_index].get_name() == expected_name

    @pytest.mark.parametrize("bun_index, expected_price", [
        (0, 100),
        (1, 200),
        (2, 300)
    ])
    def test_bun_get_price(self, bun_index, expected_price):
        assert self.buns[bun_index].get_price() == expected_price
