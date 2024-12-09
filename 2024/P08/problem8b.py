from collections import defaultdict

data = []
with open("problem8.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

def gcd(a, b):
    M = max(abs(a), abs(b))
    m = min(abs(a), abs(b))
    while m > 0:
        r = M % m
        M = m
        m = r
    return M

antinodes = set()
antennae = defaultdict(set)
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c != '.':
            antennae[c].add((i, j))

for c, points in antennae.items():
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue

            dx, dy = (p2[0] - p1[0], p2[1] - p1[1])
            g = gcd(dx, dy)
            mindx = dx // g
            mindy = dy // g

            p3 = p1
            while 0 <= p3[0] - mindx < len(data) and 0 <= p3[1] - mindy < len(data[0]):
                p3 = (p3[0] - mindx, p3[1] - mindy)

            while 0 <= p3[0] < len(data) and 0 <= p3[1] < len(data[0]):
                antinodes.add(p3)
                p3 = (p3[0] + mindx, p3[1] + mindy)

print(len(antinodes))
