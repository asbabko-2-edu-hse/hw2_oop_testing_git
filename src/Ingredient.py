class Ingredient:
  def _init_(self, name: str, quantity: float, unit: str) -> None:
    self.name = name
    self.quantity = quantity
    self.unit = unit

  @property
  def quantity(self) -> float:
    return self._quantity

  @quantity.setter
  def quantity(self, value: float) -> None:
    if value <= 0:
      raise ValueError("Количество должно быть положительным")
    self._quantity = value

  def _str_(self) -> str:
    return f"{self.name}: {self.quantity} {self.unit}"

  def _repr_(self) -> str:
    return f"Ingredient({self.name}, {self.quantity}, {self.unit})"

  def _eq_(self, other: object) -> bool:
    if not isinstance(other, Ingredient):
            return NotImplemented
    return self.name == other.name and self.unit == other.unit
