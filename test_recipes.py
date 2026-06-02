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
