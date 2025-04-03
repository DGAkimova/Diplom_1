from praktikum.bun import Bun
from data.data_buns import DataBuns

class TestBun:
    def test_get_name(self):
        bun = Bun(DataBuns.NAME_BUN,DataBuns.PRICE_BUN)
        assert bun.get_name() == DataBuns.NAME_BUN

    def test_get_price(self):
        bun = Bun(DataBuns.NAME_BUN,DataBuns.PRICE_BUN)
        assert bun.get_price() == DataBuns.PRICE_BUN