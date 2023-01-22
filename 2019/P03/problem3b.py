data = []
with open("problem3.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

wire1 = data[0].split(',')
wire2 = data[1].split(',')

wire1 = [(s[0], int(s[1:])) for s in wire1]
wire2 = [(s[0], int(s[1:])) for s in wire2]

wire1_points = {}
wire2_points = {}

def add_points_in_line(s, inst, x, y, steps):
    for i in range(inst[1]):
        steps += 1
        direc = inst[0]
        if direc == 'U':
            y = y + 1
        elif direc == 'D':
            y = y - 1
        elif direc == 'R':
            x = x + 1
        elif direc == 'L':
            x = x - 1
        s[(x, y)] = steps
    return x, y, steps

def get_wire_dist(w1, w2, p):
    return w1[p] + w2[p]

x, y = (0, 0)
steps = 0
for inst in wire1:
    x, y, steps = add_points_in_line(wire1_points, inst, x, y, steps)

x, y = (0, 0)
steps = 0
for inst in wire2:
    x, y, steps = add_points_in_line(wire2_points, inst, x, y, steps)

both_points = set(wire1_points) & set(wire2_points)
dists = [get_wire_dist(wire1_points, wire2_points, p) for p in both_points]
print(min(dists))
