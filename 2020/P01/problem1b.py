data = [int(datum) for datum in open("problem1.txt", 'r').readlines()]
for i, d1 in enumerate(data):
    for j, d2 in enumerate(data[i + 1:]):
        if 2020 - d1 - d2 in data[i + 1:i + 1 + j] + data[i + 2 + j:]:
            print(d1 * d2 * (2020 - d1 - d2))
            break
