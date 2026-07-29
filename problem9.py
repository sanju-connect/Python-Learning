p1 = "Make a Lot of Money"
p2 = "Buy Now"
p3 = "Subscribe This"
p4 = "Click This"

message = input("Enter Your Comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("Comment is not a spam")