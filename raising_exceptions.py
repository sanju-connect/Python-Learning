a = input("Enter First Number: ")
b = input("Enter Second Number: ")

if(b == 0):
    raise ZeroDivisionError("Hey out program is not meant to divide numbers by zero")
else:
    print(f"The Division a/b is {a/b}")
