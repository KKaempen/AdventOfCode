from string import ascii_lowercase, ascii_uppercase

data = []
with open("problem3.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

vals = {ascii_lowercase[i]: i + 1 for i in range(26)} 
for i in range(26, 52):
    vals[ascii_uppercase[i - 26]] = i + 1

total = 0
i = 0
while i < len(data):
    d1 = data[i]
    d2 = data[i + 1]
    d3 = data[i + 2]
    i += 3
    common = set({})
    for c in d1:
        if c in d2:
            common.add(c)
    for c in d3:
        if c in common:
            total += vals[c]
            break

print(total)

