data = []
with open("problem1.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data]

total = 0
for d in data:
    total += d // 3 - 2

print(total)
