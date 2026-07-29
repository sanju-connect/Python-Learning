def greatest(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c > a and c > b):
        return c
    else:
        print(f"Invalid Integer")


a = int(input("Enter First Number: "))
b = int(input("Enter Se4cond Number: "))
c = int(input("Enter Third Number: "))

print(f"The Gratest Integer Between {a} and {b} and {c} is: {greatest(a, b, c)}")
