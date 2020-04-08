from typing import List
class TypeHint:

  x : str = "Hello String"
  i: bool = True

  def list_avg(sequence: list) -> float:
    return sum(sequence)/len(sequence)

  def ret_class(self)->"TypeHint":
    th = TypeHint()
    return th

  def more_var(self, s: str, i: int) -> bool:
    return True

  list_avg([1,2,3])
