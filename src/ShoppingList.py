from src.Recipe import Recipe
from src.Ingredient import Ingredient
from typing import List, Tuple

class ShoppingList:
  def __init__(self) -> None:
    self._items: List[Tuple[Ingredient, str]] = []

  def add_recipe(self, recipe: Recipe, portions: float) -> None:
    if portions <= 0:
      raise ValueError("Количество порций должно быть положительным")
    updatedRecipe = recipe.scale(portions)
    for x in updatedRecipe._ingredients:
      self._items.append((x, recipe.title))
  
  def remove_recipe(self, title: str) -> None:
    updatedItems = []
    for x in self._items:
      if x[1] != title:
        updatedItems.append(x)
    self._items = updatedItems

  def get_list(self) -> List[Ingredient]:
    sList = {}
    for x, recipe_title in self._items:
      key = (x.name, x.unit)
      if key in sList:
        sList[key] += x.quantity
      else:
        sList[key] = x.quantity
    shoppingList = []
    for (name, unit), quantity in sList.items():
      shoppingList.append(Ingredient(name, quantity, unit))
    shoppingList.sort(key=lambda y: y.name)
    return shoppingList

  def __add__(self, other: 'ShoppingList') -> 'ShoppingList':
    nList = ShoppingList()
    nList._items = self._items.copy()
    nList._items.extend(other._items)
    return nList
