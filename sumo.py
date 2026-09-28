class chankonabe():
  def __init__(self):
    self.ingredients = []
    self.delicious = True

  def is_delicious(self):
    return self.delicious

class rikishi():
  def __init__(self, name, height, weight, age, rank):
    self.name = name
    self.height = height
    self.weight = weight
    self.age = age
    self.rank = rank
    self.last_ten = {} # Dict of last 10 results {<opponent>: <result>}
    self.record = {} # Dict of last 12 months of tournament results
    self.rank_history = {} # Dict of last 12 months of rank history (should go hand in hand with tournament results)
  
  def __str__(self):
    return self.name


def main():
  chanko = chankonabe()
  print(f"Is the chanko delicious? {chanko.is_delicious()}")

  r = rikishi("Chanko", 190, 182, 22, "M10")
  print(r)

main()
