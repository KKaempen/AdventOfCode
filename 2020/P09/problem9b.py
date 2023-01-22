data = [int(x) for x in open('problem9.txt', 'r').read().splitlines()]

num = 22406676

for k in range(2, len(data)):
    for i in range(len(data) + 1 - k):
        if sum(data[i:i + k]) == num:
            print(max(data[i:i + k]) + min(data[i:i + k]))

