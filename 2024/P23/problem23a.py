from collections import defaultdict

data = []
with open("problem23.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

connections = defaultdict(set)
for line in data:
    n1, n2 = line.split('-')
    connections[n1].add(n2)
    connections[n2].add(n1)

sets_of_3 = set()
for n1 in connections:
    for n2 in connections[n1]:
        valid = connections[n1] & connections[n2]
        for v in valid:
            l = sorted([n1, n2, v])
            t = tuple(l)
            sets_of_3.add(t)

print(len([x for x in sets_of_3 if any(v[0] == 't' for v in x)]))
