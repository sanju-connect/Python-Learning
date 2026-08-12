class Complex:
    def __init__(self, r, j):
        self.r = r
        self.j = j
    def __add__(self):
        return (self.r + self.j)

    def __str__(self):
        return f"{self.r} + {self.j}i"

z = Complex(3, 4)

print(z)
