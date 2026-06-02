import pytest
from src.Ingredient import Ingredient

def test_create_ingredient():
  ingredient = Ingredient("Мука", 500.0, "г")
  assert ingredient.name == "Мука"
  assert ingredient.quantity == 500.0
  assert ingredient.unit == "г"

def test_ingredient_str():
  ingredient = Ingredient("Мука", 500.0, "г")
  assert str(ingredient) == "Мука: 500.0 г"

def test_ingredient_equal_if_different_quantity():
  ingredient1 = Ingredient("Мука", 500.0, "г")
  ingredient2 = Ingredient("Мука", 250.0, "г")
  assert ingredient1 == ingredient2

def test_ingredient_equal_if_different_name():
  ingredient1 = Ingredient("Мука", 500.0, "г")
  ingredient2 = Ingredient("Сахар", 500.0, "г")
  assert ingredient1 != ingredient2

def test_ingredient_equal_if_different_unit():
  ingredient1 = Ingredient("Мука", 500.0, "г")
  ingredient2 = Ingredient("Мука", 1.0, "кг")
  assert ingredient1 != ingredient2
import pytest
from src.ShoppingList import ShoppingList
from src.Recipe import Recipe
from src.Ingredient import Ingredient

def test_add_recipe():
  ingredients = [Ingredient("Мука", 150.0, "г"), Ingredient("Вишня", 150.0, "г"), Ingredient("Шоколад", 200.0, "г")]
  recipe = Recipe("Брауни с вишней", ingredients)
  shoppingList = ShoppingList()
  shoppingList.add_recipe(recipe, 2)
  assert len(shoppingList._items) == 3

def test_add_recipe_inappropriate_portions():
  ingredients = [Ingredient("Мука", 150.0, "г"), Ingredient("Вишня", 150.0, "г"), Ingredient("Шоколад", 200.0, "г")]
  recipe = Recipe("Брауни с вишней", ingredients)
  shoppingList = ShoppingList()
  with pytest.raises(ValueError, match = "Количество порций должно быть положительным"):
    shoppingList.add_recipe(recipe, -1)

def test_remove_recipe():
  ingredients1 = [Ingredient("Мука", 150.0, "г"), Ingredient("Вишня", 150.0, "г"), Ingredient("Шоколад", 200.0, "г")]
  recipe1 = Recipe("Брауни с вишней", ingredients1)
  ingredients2 = [Ingredient("Вода", 200.0, "г"), Ingredient("Сыр", 300.0, "г")]
  recipe2 = Recipe("Хачапури", ingredients2)
  shoppingList = ShoppingList()
  shoppingList.add_recipe(recipe1, 1)
  shoppingList.add_recipe(recipe2, 1)
  assert len(shoppingList._items) == 5
  shoppingList.remove_recipe("Брауни с вишней")
  assert len(shoppingList._items) == 2
  assert shoppingList._items[0][1] == "Хачапури"

def test_remove_none_recipe():
  shoppingList = ShoppingList()
  shoppingList.remove_recipe("Брауни с вишней")
  assert len(shoppingList._items) == 0

def test_get_list():
  ingredients1 = [Ingredient("Мука", 150.0, "г"), Ingredient("Вишня", 150.0, "г"), Ingredient("Шоколад", 200.0, "г")]
  recipe1 = Recipe("Брауни с вишней", ingredients1)
  ingredients2 = [Ingredient("Мука", 300.0, "г"), Ingredient("Вода", 200.0, "г"), Ingredient("Сыр", 300.0, "г")]
  recipe2 = Recipe("Хачапури", ingredients2)
  shoppingList = ShoppingList()
  shoppingList.add_recipe(recipe1, 1)
  shoppingList.add_recipe(recipe2, 1)
  sList = shoppingList.get_list()
  assert len(sList) == 5
  assert sList[2].name == "Мука"
  assert sList[2].quantity == 450.0

def test_get_list_sort():
  ingredients1 = [Ingredient("Мука", 150.0, "г"), Ingredient("Вишня", 150.0, "г"), Ingredient("Шоколад", 200.0, "г")]
  recipe1 = Recipe("Брауни с вишней", ingredients1)
  ingredients2 = [Ingredient("Мука", 300.0, "г"), Ingredient("Вода", 200.0, "г"), Ingredient("Сыр", 300.0, "г")]
  recipe2 = Recipe("Хачапури", ingredients2)
  shoppingList = ShoppingList()
  shoppingList.add_recipe(recipe1, 1)
  shoppingList.add_recipe(recipe2, 1)
  sList = shoppingList.get_list()
  assert sList[0].name == "Вишня"

def test_add():
  ingredients1 = [Ingredient("Мука", 150.0, "г"), Ingredient("Вишня", 150.0, "г"), Ingredient("Шоколад", 200.0, "г")]
  recipe1 = Recipe("Брауни с вишней", ingredients1)
  ingredients2 = [Ingredient("Вода", 200.0, "г"), Ingredient("Сыр", 300.0, "г")]
  recipe2 = Recipe("Хачапури", ingredients2)
  shoppingList1 = ShoppingList()
  shoppingList2 = ShoppingList()
  shoppingList1.add_recipe(recipe1, 1)
  shoppingList2.add_recipe(recipe2, 1)
  sList = shoppingList1 + shoppingList2
  assert len(sList._items) == 5
  assert len(shoppingList1._items) == 3
  assert len(shoppingList2._items) == 2
