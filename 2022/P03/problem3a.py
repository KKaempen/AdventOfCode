from string import ascii_lowercase, ascii_uppercase

data = []
with open("problem3.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

vals = {ascii_lowercase[i]: i + 1 for i in range(26)} 
for i in range(26, 52):
    vals[ascii_uppercase[i - 26]] = i + 1

total = 0
for d in data:
    d1 = d[:len(d) // 2]
    d2 = d[len(d) // 2:]
    for c in d1:
        if c in d2:
            total += vals[c]
            break

print(total)

