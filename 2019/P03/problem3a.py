data = []
with open("problem3.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

wire1 = data[0].split(',')
wire2 = data[1].split(',')

wire1 = [(s[0], int(s[1:])) for s in wire1]
wire2 = [(s[0], int(s[1:])) for s in wire2]

wire1_points = set({})
wire2_points = set({})

def add_points_in_line(s, inst, x, y):
    for i in range(inst[1]):
        direc = inst[0]
        if direc == 'U':
            y = y + 1
        elif direc == 'D':
            y = y - 1
        elif direc == 'R':
            x = x + 1
        elif direc == 'L':
            x = x - 1
        s.add((x, y))
    return x, y

def get_man_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

x, y = (0, 0)
for inst in wire1:
    x, y = add_points_in_line(wire1_points, inst, x, y)

x, y = (0, 0)
for inst in wire2:
    x, y = add_points_in_line(wire2_points, inst, x, y)

both_points = wire1_points & wire2_points
origin = (0, 0)
dists = [get_man_dist(origin, p) for p in both_points]
print(min(dists))
