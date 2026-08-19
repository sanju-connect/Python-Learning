from functools import reduce

l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqList = map(square, l)
print(list(sqList))

# Example of Filter

def even(n):
    return n % 2 == 0

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Function

def sum(a, b):
    return a + b


print(reduce(sum, l))
