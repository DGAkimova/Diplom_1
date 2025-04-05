from praktikum.ingredient import Ingredient
from data.data_buns import DataBuns

class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(DataBuns.TYPE_INGREDIENT,DataBuns.NAME_INGREDIENT,DataBuns.PRICE_INGREDIENT)
        assert ingredient.get_price() == DataBuns.PRICE_INGREDIENT

    def test_get_name(self):
        ingredient = Ingredient(DataBuns.TYPE_INGREDIENT,DataBuns.NAME_INGREDIENT,DataBuns.PRICE_INGREDIENT)
        assert ingredient.get_name() == DataBuns.NAME_INGREDIENT

    def test_get_type(self):
        ingredient = Ingredient(DataBuns.TYPE_INGREDIENT,DataBuns.NAME_INGREDIENT,DataBuns.PRICE_INGREDIENT)
        assert ingredient.get_type() == DataBuns.TYPE_INGREDIENT