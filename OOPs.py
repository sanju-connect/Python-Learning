class Employee:
    language = "Py"
    salary = 120000
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
    print("i am Creating an Object")

    def getInfo(self):
        print(f"The Languages is: {self.language}. The Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


sanju = Employee("Sanju", "Python", 120000)

print(sanju.name, sanju.language, sanju.salary)