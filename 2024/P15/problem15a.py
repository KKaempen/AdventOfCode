data = []
with open("problem15.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

box, insts = '\n'.join(data).split('\n\n')
warehouse = []
robot_start = None
for i, line in enumerate(box.split('\n')):
    row = []
    for j, c in enumerate(line):
        if c == '@':
            robot_start = (i, j)
        row.append(c)
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

    tx, ty = nx, ny
    while warehouse[tx][ty] == 'O':
        tx, ty = (tx + dx, ty + dy)

    if warehouse[tx][ty] == '#':
        continue

    warehouse[tx][ty] = 'O'
    warehouse[nx][ny] = '@'
    warehouse[rx][ry] = '.'
    robot_pos = (nx, ny)

total = 0
for i, line in enumerate(warehouse):
    for j, c in enumerate(line):
        if c != 'O':
            continue
        total += 100 * i + j

print(total)
