class Calculator:
  def _init_(self, n):
    self.n = n

  def square(self):
    print(f"The Square is: {self.n * self.n}")

  def qube(self):
      print(f"The Square is: {self.n * self.n * self.n}")

  def square_root(self):
      print(f"The Square Root is: {self.n ** 0.5}")


a = Calculator(5)
a.square()