data = []
with open("problem22.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data]

prune_val = 16777216
total = 0
for num in data:
    for i in range(2000):
        r = num * 64
        num = (num ^ r) % prune_val
        r = num // 32
        num = (num ^ r) % prune_val
        r = num * 2048
        num = (num ^ r) % prune_val
    total += num
print(total)
