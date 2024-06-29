from praktikum.database import Database


class TestDatabase:
    def test_database_initialization(self):
        db = Database()
        assert db.data == []

    def test_database_add_burger(self, mock_burger):
        db = Database()
        db.add_burger(mock_burger)
        assert mock_burger in db.data

    def test_database_get_all_burgers(self, mock_burger):
        db = Database()
        db.add_burger(mock_burger)
        assert db.get_all_burgers() == [mock_burger]
