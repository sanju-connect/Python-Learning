class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __len__(self):
        return len(Vector(self.x + self.y + self.z))

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


v1 = Vector(1, 2, 3)
print(len(v1))
