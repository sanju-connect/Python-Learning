dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
merged = dic1 | dic2

print(merged)

with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
