def Factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * Factorial(n-1)


n = int(input("Enter a Number: "))

print(f"The Factorial of {n} is: {Factorial(n)}")


# Factorial (5)
# 5 * Factorial(4)
# 5 * 4 * Factorial(3)
# 5 * 4 * 3 * Factorial(2)
# 5 * 4 * 3 * 2 * Factorial(1)
# 5 * 4 * 3 * 2 * 1