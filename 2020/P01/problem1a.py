data = [int(datum) for datum in open("problem1.txt", 'r').readlines()]

for i, d in enumerate(data):
    if 2020 - d in data[:i] + data[i + 1:]:
        print((2020 - d) * d)
        break
