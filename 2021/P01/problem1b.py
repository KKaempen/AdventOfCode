data = [int(datum) for datum in open("problem1.txt", 'r').readlines()]

past = data[0]
count = 0
for i, d in enumerate(data[3:]):
    if d > past:
        count += 1
    past = data[i + 1]

print(count)
