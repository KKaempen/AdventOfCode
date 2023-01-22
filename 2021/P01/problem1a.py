data = [int(datum) for datum in open("problem1.txt", 'r').readlines()]

past = data[0]
count = 0
for d in data[1:]:
    if d > past:
        count += 1
    past = d

print(count)
