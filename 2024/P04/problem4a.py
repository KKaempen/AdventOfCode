import re

data = []
with open("problem4.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

n = len(data)
m = len(data[0])
data += [''.join([data[j][i] for j in range(n)]) for i in range(m)]
data += [''.join([data[i + j][j] for j in range(min(m, n - i))]) for i in range(n)] + [''.join([data[i][j + i] for i in range(min(n, m - j))]) for j in range(1, m)]
data += [''.join([data[n - 1 - (i + j)][j] for j in range(min(m, n - i))]) for i in range(n)] + [''.join([data[n - 1 - i][j + i] for i in range(min(n, m - j))]) for j in range(1, m)]

regex = re.compile('(?=(XMAS|SAMX))')
count = sum([len(regex.findall(line)) for line in data])

print(count)
