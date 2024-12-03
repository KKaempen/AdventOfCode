data = []
with open("problem2.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

count = 0
for line in data:
    report = [int(x) for x in line.split()]
    if (
        all(x < y for x, y in zip(report[:-1], report[1:])) or
        all(x > y for x, y in zip(report[:-1], report[1:]))
        ) and all(abs(x - y) <= 3 for x, y in zip(report[:-1], report[1:])):
        count += 1
print(count)
