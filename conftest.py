import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import random
import string

@pytest.fixture()
def mock_ingridients():
    letters = string.ascii_lowercase
    mock_ingredients = Mock()
    mock_ingredients.type = INGREDIENT_TYPE_SAUCE
    mock_ingredients.name = ''.join(random.choice(letters) for i in range(10))
    mock_ingredients.price = 25
    return mock_ingredients