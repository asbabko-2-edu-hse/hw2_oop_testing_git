class Recipe:
  def __init__(self, title: str, ingredients: list = None) -> None:
    self.title = title
    self._ingredients = ingredients

  def add_ingredient(self, ingredient: Ingredient) -> None:
    for x in self._ingredients:
      if x == ingredient:
        x.quantity += ingredient.quantity
        return
    self._ingredients.append(ingredient)

  @staticmethod
  def is_valid_ratio(ratio) -> bool:
    return float(ratio) > 0

  def scale(self, ratio: float):
    if self.is_valid_ratio(ratio):
      ratio = float(ratio)
      updatedIngredients = []
      for x in self._ingredients:
        updatedIngredient = Ingredient(x.name, x.quantity * ratio, x.unit)
        updatedIngredients.append(updatedIngredient)
      return Recipe(self.title, updatedIngredients)

  def __len__(self) -> int:
    return len(self._ingredients)

  def __str__(self) -> str:
    recipe = f"Рецепт '{self.title}':\n"
    for x in self._ingredients:
      recipe += f" - {x}\n"
    return recipe
