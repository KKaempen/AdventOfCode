data = []
with open("problem4.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

count = 0
for i in range(len(data) - 2):
    for j in range(len(data[i]) - 2):
        l1 = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2]
        l2 = data[i][j + 2] + data[i + 1][j + 1] + data[i + 2][j]
        if (l1 == 'MAS' or l1 == 'SAM') and (l2 == 'MAS' or l2 == 'SAM'):
            count += 1

print(count)
