n = int(input("Enter a Number: "))

for i in range(1, n):
    if(n%i == 0):
        print("Number is Not Prime Number")
        break

    else:
        print("Number is Not Prime")

for i in range(1, (n+1)):
    print(" " * (n - i), end="")
    print("*" * (2*i-1), end="")
    print("\n")

for i in range(1, n+1):
    print("*" * i)
    print("\n")

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("\n")