class DietaryRecipe(Recipe):
  def __init__(self, title: str, diet_type: str, ingredients: Optional[List[Ingredient]] = None) -> None:
    super().__init__(title, ingredients)
    self.diet_type = diet_type
  
  def scale(self, ratio: float) -> DietaryRecipe:
    updatedRecipe = super().scale(ratio)
    return DietaryRecipe(title = updatedRecipe.title, diet_type = self.diet_type, ingredients = updatedRecipe._ingredients)

  def __str__(self) -> str:
    return f'["{self.diet_type}"] {self.title}'
