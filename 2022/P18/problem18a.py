data = []
with open("problem18.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

cubes = set({})
for d in data:
    cubes.add(tuple([int(x) for x in d.split(',')]))

def get_adj(c):
    x, y, z = c
    adj = []
    for i in {-1, 1}:
        adj.append((x + i, y, z))
        adj.append((x, y + i, z))
        adj.append((x, y, z + i))
    return adj

num_hidden_sides = 0
for c in cubes:
    adj = get_adj(c)
    for a in adj:
        if a in cubes:
            num_hidden_sides += 1

print(len(cubes) * 6 - num_hidden_sides)
