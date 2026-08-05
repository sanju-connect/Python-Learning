class Employee:
    a = 1

class Programmer(Employee):
    b = 1

class Manager(Programmer):
    c = 3

o = Manager()
print(o.a)
