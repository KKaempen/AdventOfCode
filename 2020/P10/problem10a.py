data = [int(x) for x in open('problem10.txt', 'r').read().splitlines()] + [0]

data.sort()
data.append(data[len(data) - 1] + 3)

num1s = 0
num3s = 0
for i in range(1, len(data)):
    if data[i] - data[i - 1] == 3:
        num3s += 1
    if data[i] - data[i - 1] == 1:
        num1s += 1

print(num1s * num3s)
