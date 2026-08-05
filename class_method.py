class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The Value of a is: {self.a}")


e = Employee()
e.a = 45
e.name = "Sanju"
print(e.name)
e.show()
