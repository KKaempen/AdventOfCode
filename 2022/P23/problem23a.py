data = []
with open("problem23.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')
    
positions = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        positions[(i, j)] = True if data[i][j] == '#' else False

def check_north(p):
    y, x = p
    return [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1)]

def check_south(p):
    y, x = p
    return [(y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]

def check_west(p):
    y, x = p
    return [(y - 1, x - 1), (y, x - 1), (y + 1, x - 1)]

def check_east(p):
    y, x = p
    return [(y - 1, x + 1), (y, x + 1), (y + 1, x + 1)]

def get_all_adj(p):
    y, x = p
    return [(y - 1, x - 1), (y - 1, x),
            (y - 1, x + 1), (y, x + 1),
            (y + 1, x + 1), (y + 1, x),
            (y + 1, x - 1), (y, x - 1)]

def include_surroundings(d):
    to_add = []
    for p in d:
        points = get_all_adj(p)
        for p2 in points:
            if p2 in d:
                continue
            to_add.append(p2)
    for p in to_add:
        d[p] = False

def run_iteration(d, dirs):
    include_surroundings(d)
    proposed_moves = {}
    for p in (p for p in d if d[p]):
        all_adj = get_all_adj(p)
        elf_exists = False
        for p2 in all_adj:
            if d[p2]:
                elf_exists = True
                break
        if not elf_exists:
            continue
        for f in dirs:
            ps = f(p)
            can_move = True
            for p2 in ps:
                if d[p2]:
                    can_move = False
                    break
            if can_move:
                dest = ps[1]
                if dest not in proposed_moves:
                    proposed_moves[dest] = []
                proposed_moves[dest].append(p)
                break
    for dest in proposed_moves:
        ps = proposed_moves[dest]
        if len(ps) == 1:
            p = ps[0]
            d[p] = False
            d[dest] = True

dirs = [check_north, check_south, check_west, check_east]
for i in range(10):
    run_iteration(positions, dirs)
    f = dirs.pop(0)
    dirs.append(f)

elf_positions = [x for x in positions if positions[x]]
elf_ys = [x[0] for x in elf_positions]
elf_xs = [x[1] for x in elf_positions]
y_max = max(elf_ys)
y_min = min(elf_ys)
x_max = max(elf_xs)
x_min = min(elf_xs)
print((x_max - x_min + 1) * (y_max - y_min + 1) - len(elf_positions))
