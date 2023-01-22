data = []
with open("problem17.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = data[0]
rocks = [[['#', '#', '#', '#']], [['.', '#', '.'], ['#', '#', '#'], ['.', '#', '.']], [['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#']], [['#'], ['#'], ['#'], ['#']], [['#', '#'], ['#', '#']]]

floor = [['.' for i in range(7)] for j in range(4)]

def print_rock(r):
    print()
    for row in r[::-1]:
        print(''.join(row))
    print()

def print_floor(area):
    for r in area[::-1]:
        print('|' + ''.join(r) + '|')
    print('-' * 9)
    print()

def settle_rock(area, r, pos):
    y, x = pos
    for j in range(len(r)):
        for i in range(len(r[j])):
            if r[j][i] == '#':
                area[y + j][x + i] = '#'

def check_intersect(area, r, pos):
    y, x = pos
    for j in range(len(r)):
        for i in range(len(r[j])):
            if r[j][i] == '#' and area[y + j][x + i] == '#':
                return True
    return False

def try_move_side(area, r, pos, mv):
    w = len(r[0])
    y, x = pos
    if x + mv < 0 or x + mv + w > 7 or check_intersect(area, r, (y, x + mv)):
        return pos
    return (y, x + mv)

def try_move_down(area, r, pos):
    w = len(r[0])
    y, x = pos
    if y - 1 < 0 or check_intersect(area, r, (y - 1, x)):
        settle_rock(area, r, pos)
        return pos
    return (y - 1, x)

def simulate_fall(area, r, height, jet_idx):
    h = len(r)
    pos = (height + 4, 2)
    if pos[0] + h > len(area):
        diff = pos[0] + h - len(area)
        area += [['.' for i in range(7)] for j in range(diff)]
    while True:
        if data[jet_idx] == '<':
            pos = try_move_side(area, r, pos, -1)
        elif data[jet_idx] == '>':
            pos = try_move_side(area, r, pos, 1)
        jet_idx += 1
        jet_idx %= len(data)
        new_pos = try_move_down(area, r, pos)
        if new_pos == pos:
            break
        pos = new_pos
    return max(h + pos[0] - 1, height), jet_idx

rock_height = -1
jet_idx = 0
for i in range(2022):
    rock_height, jet_idx = simulate_fall(floor, rocks[i % 5], rock_height, jet_idx)

print(rock_height + 1)
