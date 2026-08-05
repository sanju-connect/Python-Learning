class Programmer:
  company = "Microsoft"
  def _init_(self, name, salary, pin):
    self.name = name
    self.salary = salary
    self.pin = pin


p = Programmer("Sanju", 120000, 734014)
print(p.name, p.salary, p.pin, p.company)