data = []
with open("problem9.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

def print_rope(rope):
    return
    y_min = min(0, min([t[1] for t in rope]))
    x_min = min(0, min([t[0] for t in rope]))
    y_max = max([t[1] for t in rope])
    x_max = max([t[0] for t in rope])
    for j in range(y_max, y_min - 1, -1):
        for i in range(x_min, x_max + 1):
            p = (i, j)
            if p not in rope:
                print('.', end='')
            else:
                idx = rope.index(p)
                idx = 'H' if idx == 0 else str(idx)
                print(idx, end='')
        print()
    print()

def get_new_t_pos(h_pos, t_pos, v=None):
    d_x = h_pos[0] - t_pos[0]
    x_m = 0 if d_x == 0 else d_x // abs(d_x)
    d_y = h_pos[1] - t_pos[1]
    y_m = 0 if d_y == 0 else d_y // abs(d_y)
    if abs(d_x) >= 2 and abs(d_y) >= 1:
        t_pos = (t_pos[0] + x_m, t_pos[1] + y_m)
    elif abs(d_x) >= 2:
        t_pos = (t_pos[0] + x_m, t_pos[1])
    elif abs(d_x) >= 1 and abs(d_y) >= 2:
        t_pos = (t_pos[0] + x_m, t_pos[1] + y_m)
    elif abs(d_y) >= 2:
        t_pos = (t_pos[0], t_pos[1] + y_m)
    if v:
        v.add(t_pos)
    return t_pos

visited = {(0, 0)}

knot_pos = [(0, 0) for i in range(10)]
for d in data:
    inst = d.split()
    if inst[0] == 'D':
        for i in range(int(inst[1])):
            h_pos = knot_pos[0]
            knot_pos[0] = (h_pos[0], h_pos[1] - 1)
            for i in range(1, 10):
                v = None
                if i == 9:
                    v = visited
                knot_pos[i] = get_new_t_pos(knot_pos[i - 1], knot_pos[i], v)
            print_rope(knot_pos)
    if inst[0] == 'U':
        for i in range(int(inst[1])):
            h_pos = knot_pos[0]
            knot_pos[0] = (h_pos[0], h_pos[1] + 1)
            for i in range(1, 10):
                v = None
                if i == 9:
                    v = visited
                knot_pos[i] = get_new_t_pos(knot_pos[i - 1], knot_pos[i], v)
            print_rope(knot_pos)
    if inst[0] == 'L':
        for i in range(int(inst[1])):
            h_pos = knot_pos[0]
            knot_pos[0] = (h_pos[0] - 1, h_pos[1])
            for i in range(1, 10):
                v = None
                if i == 9:
                    v = visited
                knot_pos[i] = get_new_t_pos(knot_pos[i - 1], knot_pos[i], v)
            print_rope(knot_pos)
    if inst[0] == 'R':
        for i in range(int(inst[1])):
            h_pos = knot_pos[0]
            knot_pos[0] = (h_pos[0] + 1, h_pos[1])
            for i in range(1, 10):
                v = None
                if i == 9:
                    v = visited
                knot_pos[i] = get_new_t_pos(knot_pos[i - 1], knot_pos[i], v)
            print_rope(knot_pos)

print(len(visited))
