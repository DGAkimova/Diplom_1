from praktikum.burger import Burger
from data.data_buns import DataBuns

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        burger.set_buns(DataBuns.NAME_BUN)
        assert DataBuns.NAME_BUN == burger.bun

    def test_add_ingredient(self,mock_ingridients):
        burger = Burger()
        burger.add_ingredient(mock_ingridients)
        assert mock_ingridients in burger.ingredients

    def test_remove_ingredient(self,mock_ingridients):
        burger = Burger()
        burger.add_ingredient(mock_ingridients)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self,mock_ingridients):
        burger = Burger()
        burger.add_ingredient(mock_ingridients)
        burger_1 = burger.ingredients[0]
        burger.add_ingredient(mock_ingridients)
        burger_2 = burger.ingredients[1]
        burger.move_ingredient(0,1)
        assert burger_1 == burger.ingredients[1]
        assert burger_2 == burger.ingredients[0]

