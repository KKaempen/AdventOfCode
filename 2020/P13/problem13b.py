f = open('problem13.txt', 'r').read().splitlines()
ids = [int(x) if x != 'x' else -1 for x in f[1].split(',')]

ids = [(idx, j) for j, idx in enumerate(ids) if idx != -1]
base = 1
offset = 0
for idx, off in ids:
    while (offset + off) % idx != 0:
        offset += base
    base *= idx

print(offset)

