class Employee:
  company = "ITC"
  def show(self):
    print(f"The name is {self.name} and the Salry is {self.salary}")

class Programmer(Employee):
  company = "ITC Infotech"

  def showlanguage(self):
     print(f"The name is {self.name} and He is Good with {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)