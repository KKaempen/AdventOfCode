data = []
with open("problem18.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

cubes = set({})
for d in data:
    cubes.add(tuple([int(x) for x in d.split(',')]))

def get_adj_sides(c, cubes):
    adj = []
    x, y, z, d = c
    for i in {-1, 1}:
        if d[0] == 0:
            p1 = (x + i + d[0], y + d[1], z + d[2])
            p2 = (x + i, y, z)
            if p1 in cubes:
                new_d = (-i, 0, 0)
                adj.append((*p1, new_d))
            elif p2 in cubes:
                adj.append((*p2, d))
            else:
                new_d = (i, 0, 0)
                adj.append((x, y, z, new_d))
        if d[1] == 0:
            p1 = (x + d[0], y + i + d[1], z + d[2])
            p2 = (x, y + i, z)
            if p1 in cubes:
                new_d = (0, -i, 0)
                adj.append((*p1, new_d))
            elif p2 in cubes:
                adj.append((*p2, d))
            else:
                new_d = (0, i, 0)
                adj.append((x, y, z, new_d))
        if d[2] == 0:
            p1 = (x + d[0], y + d[1], z + i + d[2])
            p2 = (x, y, z + i)
            if p1 in cubes:
                new_d = (0, 0, -i)
                adj.append((*p1, new_d))
            elif p2 in cubes:
                adj.append((*p2, d))
            else:
                new_d = (0, 0, i)
                adj.append((x, y, z, new_d))
    return adj

min_x_cube = min(cubes)
seen_faces = set({})
frontier = [(*min_x_cube, (-1, 0, 0))]
while len(frontier) > 0:
    curr = frontier.pop(0)
    if curr in seen_faces:
        continue
    seen_faces.add(curr)
    for s in get_adj_sides(curr, cubes):
        frontier.append(s)

print(len(seen_faces))
