data = []
with open("problem22.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = '\n'.join(data).split('\n\n')
maze = data[0].split('\n')
path = data[1]

maze_width = max([len(r) for r in maze])
for i in range(len(maze)):
    r = maze[i]
    if len(r) < maze_width:
        maze[i] = r + " " * (maze_width - len(r))

path = path.split('L')
p = []
for e in path:
    if 'R' in e:
        p2 = e.split('R')
        for e2 in p2[:-1]:
            p.append(int(e2))
            p.append('R')
        p.append(int(p2[-1]))
        p.append('L')
    else:
        p.append(int(e))
        p.append('L')
p = p[:-1]

pos = (0, maze[0].index('.'))
d = (0, 1)
for inst in p:
    dy, dx = d
    if inst == 'L':
        d = (-dx, dy)
    elif inst == 'R':
        d = (dx, -dy)
    else:
        y, x = pos
        last_y, last_x = pos
        for i in range(inst):
            y = (y + dy) % len(maze)
            x = (x + dx) % len(maze[y])
            if maze[y][x] == ' ':
                while maze[y][x] == ' ':
                    y = (y + dy) % len(maze)
                    x = (x + dx) % len(maze[y])
                    pos = (y + dy, x + dx)
            if maze[y][x] == '.':
                last_y, last_x = y, x
            if maze[y][x] == '#':
                pos = (last_y, last_x)
                break
            pos = (y, x)

facing = 0 if d == (0, 1) else 1 if d == (1, 0) else 2 if d == (0, -1) else 3
print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing)
