from collections import defaultdict

data = []
with open("problem8.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

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
            p3 = (p2[0] + dx, p2[1] + dy)
            p4 = (p1[0] - dx, p1[1] - dy)
            if 0 <= p3[0] < len(data) and 0 <= p3[1] < len(data[0]):
                antinodes.add(p3)
            if 0 <= p4[0] < len(data) and 0 <= p4[1] < len(data[0]):
                antinodes.add(p4)

print(len(antinodes))
