class TestBun:
    def test_bun_get_name(self, database):
        bun = database.available_buns()[0]
        assert bun.get_name() == "black bun"

    def test_bun_get_price(self, database):
        bun = database.available_buns()[1]
        assert bun.get_price() == 200
