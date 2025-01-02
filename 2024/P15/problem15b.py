data = []
with open("problem15.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

box, insts = '\n'.join(data).split('\n\n')
warehouse = []
robot_start = None
expand_map = {
    '#': '##',
    'O': '[]',
    '.': '..',
    '@': '@.',
}

for i, line in enumerate(box.split('\n')):
    row = []
    for j, c in enumerate(line):
        if c == '@':
            robot_start = (i, 2 * j)
        for nc in expand_map[c]:
            row.append(nc)
    warehouse.append(row)

dir_map = {
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
}
insts = insts.replace('\n', '')
robot_pos = robot_start
for inst in insts:

    rx, ry = robot_pos
    dx, dy = dir_map[inst]
    nx, ny = (rx + dx, ry + dy)

    if warehouse[nx][ny] == '.':
        warehouse[rx][ry] = '.'
        warehouse[nx][ny] = '@'
        robot_pos = (nx, ny)
        continue
    elif warehouse[nx][ny] == '#':
        continue

    if dx == 0:
        tx, ty = nx, ny
        dist = 0
        while warehouse[tx][ty] in {'[', ']'}:
            dist += 1
            tx, ty = (tx + dx, ty + dy)

        if warehouse[tx][ty] == '#':
            continue

        for i in range(dist):
            warehouse[tx][ty] = warehouse[tx - dx][ty - dy]
            tx, ty = (tx - dx, ty - dy)

        warehouse[nx][ny] = '@'
        warehouse[rx][ry] = '.'
        robot_pos = (nx, ny)
        continue

    to_push = [{(rx, ry)}]

    no_wall = True
    all_empty = False
    while no_wall and not all_empty:
        next_push = set()
        all_empty = True
        for cx, cy in to_push[-1]:
            if warehouse[cx][cy] == '.':
                continue
            tx, ty = (cx + dx, cy + dy)
            if warehouse[tx][ty] != '.':
                all_empty = False

            next_push.add((tx, ty))

            if warehouse[tx][ty] == '#':
                no_wall = False
                break
            elif warehouse[tx][ty] == '[':
                next_push.add((tx, ty + 1))
            elif warehouse[tx][ty] == ']':
                next_push.add((tx, ty - 1))

        to_push.append(next_push)

    if not no_wall:
        continue

    for i in range(len(to_push) - 1, 0, -1):
        for cx, cy in to_push[i]:
            fx, fy = (cx - dx, cy - dy)
            if (fx, fy) in to_push[i - 1]:
                warehouse[cx][cy] = warehouse[fx][fy]
            else:
                warehouse[cx][cy] = '.'

    warehouse[rx][ry] = '.'
    robot_pos = (nx, ny)

total = 0
for i, line in enumerate(warehouse):
    for j, c in enumerate(line):
        if c != '[':
            continue
        total += 100 * i + j

print(total)
