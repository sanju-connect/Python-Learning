list = ["Harry", "Rohan", "Subham", "an"]

def rem(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(rem(list, "an"))
