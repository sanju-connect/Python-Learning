class Employee:
  company = "ITC"
  def show(self):
    print(f"The name is {self.name} and the Salry is {self.salary}")

class Coder:
  language = "Python"
  def Print_Lan(self):
    print(f"Out of All The Languages here is your languages: {self.language}")

class Programmer(Employee, Coder):
  company = "ITC Infotech"

  def showlanguage(self):
     print(f"The name is {self.name} and He is Good with {self.language}")
