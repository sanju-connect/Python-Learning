Name = input("Enter Student Name: ")

Name_Math = int(input(f"Enter The Marks In Maths of {Name}: "))
Name_Physics = int(input(f"Enter The Marks In Physics of {Name}: "))
Name_Chemistry = int(input(f"Enter The Marks In Chemistry of {Name}: "))
Name_Biology = int(input(f"Enter The Marks In Biology of {Name}: "))
Name_Social_Science = int(input(f"Enter The Marks In Social Science of {Name}: "))

Total_Marks = ((Name_Math + Name_Physics + Name_Chemistry + Name_Biology + Name_Social_Science) / 500)

if(Total_Marks <= 100 and Total_Marks > 90):
    print(f"Grade of {Name} is: Exellent")
elif(Total_Marks <= 90 and Total_Marks > 80):
    print(f"Grade of {Name} is: A")
elif(Total_Marks <= 80 and Total_Marks > 70):
    print(f"Grade of {Name} is: B")
elif(Total_Marks <= 70 and Total_Marks > 60):
    print(f"Grade of {Name} is: C")
elif(Total_Marks <= 60 and Total_Marks > 50):
    print(f"Grade of {Name} is: D")
elif(Total_Marks <= 90 and Total_Marks >= 0):
    print(f"Grade of {Name} is: F, ")
    print(f"{Name} is Failed In The Exam")