data = [int(datum, 2) for datum in open("problem3.txt", 'r').readlines()]

data1 = [i for i in data]
data2 = [i for i in data]
for i in range(11, -1, -1):
    if len(data1) != 1:
        num_ones = 0
        for d in data1:
            num_ones += 1 if d & 2**i else 0
        data1a = []
        most_common = 2**i if num_ones >= len(data1) - num_ones else 0
        for d in data1:
            if d & 2**i == most_common:
                data1a.append(d)
        data1 = data1a
    if len(data2) != 1:
        num_ones = 0
        for d in data2:
            num_ones += 1 if d & 2**i else 0
        data2a = []
        most_common = 2**i if num_ones >= len(data2) - num_ones else 0
        for d in data2:
            if d & 2**i != most_common:
                data2a.append(d)
        data2 = data2a

print(data1[0] * data2[0])
