with open("poems.txt") as f:
    s = f.read()
    if("twinkle" in s):
        print("twinkle exist")
    else:
        print("twinkle not exist")