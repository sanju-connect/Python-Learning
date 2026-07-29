def multiply(n, j):
    for i in range(1, (j + 1)):
        print(f"{n} × {i} = {n * i}")

n = int(input("Enter The Number of Multiplicatio Table: "))
j = int(input(f"Enter The Range Till Which You Want to Print the Table of {n}: "))

multiply(n, j)