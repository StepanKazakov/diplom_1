from bun import Bun

def test_bun_initialization():
    bun = Bun("Wheat", 1.5)
    assert bun.name == "Wheat"
    assert bun.price == 1.5

def test_bun_price():
    bun = Bun("Sesame", 2.0)
    assert bun.get_price() == 2.0

def test_bun_str():
    bun = Bun("Rye", 1.0)
    assert str(bun) == "Rye: $1.0"