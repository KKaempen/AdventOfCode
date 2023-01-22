data = []
with open("problem4.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

total = 0
for d in data:
    p = d.split(',')
    l1, h1 = [int(x) for x in p[0].split('-')]
    l2, h2 = [int(x) for x in p[1].split('-')]
    if l1 >= l2 and h1 <= h2:
        total += 1
    elif l2 >= l1 and h2 <= h1:
        total += 1

print(total)

