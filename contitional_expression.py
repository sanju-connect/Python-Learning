n = input("Enter a Number: ")

if(n != int):
    print("You are an Adult")

elif(n < 0):
    print("You are entering an Invalid Age")

elif(n == 0):
    print("You are Entered an Non Valid Age")

else:
    print("You are not an Adult")

print("End of Program")