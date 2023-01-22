from math import sqrt

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

#for r in maze:
#    print(r)

cube_size = sum([r.count('.') for r in maze]) + sum([r.count('#') for r in maze])
n = int(sqrt(cube_size // 6))
maze = [maze[n * i: n * (i + 1)] for i in range(len(maze) // n)]
maze = [[[r[n * i: n * (i + 1)] for r in t] for i in range(len(t[0]) // n)] for t in maze]
maze = [[None if t[0][0] == ' ' else t for t in r] for r in maze]

class CubeFace:
    def __init__(self, data, s, o=0):
        self.s = s
        self.n = len(data)
        if o == 0:
            self.data = data.copy()
        if o == 1:
            self.data = [''.join([x[i] for x in data[::-1]]) for i in range(len(data[0]))]
        if o == 2:
            self.data = [x[::-1] for x in data[::-1]]
        if o == 3:
            self.data = [''.join([x[i] for x in data]) for i in range(len(data[0]) - 1, -1, -1)]

    def get_adj_face(self, d):
        s = self.s
        n = self.n
        if s == 'U':
            return (('F', (1, 0), lambda y, x: (0, x)) if d == (1, 0) else
                    ('L', (1, 0), lambda y, x: (0, y)) if d == (0, -1) else
                    ('R', (1, 0), lambda y, x: (0, n - y - 1)) if d == (0, 1) else
                    ('B', (1, 0), lambda y, x: (0, n - x - 1)) if d == (-1, 0) else
                    None)
        if s == 'F':
            return (('D', (1, 0), lambda y, x: (0, x)) if d == (1, 0) else
                    ('L', (0, -1), lambda y, x: (y, n - 1)) if d == (0, -1) else
                    ('R', (0, 1), lambda y, x: (y, 0)) if d == (0, 1) else
                    ('U', (-1, 0), lambda y, x: (n - 1, x)) if d == (-1, 0) else
                    None)
        if s == 'R':
            return (('D', (0, -1), lambda y, x: (x, n - 1)) if d == (1, 0) else
                    ('F', (0, -1), lambda y, x: (y, n - 1)) if d == (0, -1) else
                    ('B', (0, 1), lambda y, x: (y, 0)) if d == (0, 1) else
                    ('U', (0, -1), lambda y, x: (n - x - 1, n - 1)) if d == (-1, 0) else
                    None)
        if s == 'L':
            return (('D', (0, 1), lambda y, x: (n - x - 1, 0)) if d == (1, 0) else
                    ('B', (0, -1), lambda y, x: (y, n - 1)) if d == (0, -1) else
                    ('F', (0, 1), lambda y, x: (y, 0)) if d == (0, 1) else
                    ('U', (0, 1), lambda y, x: (x, 0)) if d == (-1, 0) else
                    None)
        if s == 'B':
            return (('D', (-1, 0), lambda y, x: (n - 1, n - x - 1)) if d == (1, 0) else
                    ('R', (0, -1), lambda y, x: (y, n - 1)) if d == (0, -1) else
                    ('L', (0, 1), lambda y, x: (y, 0)) if d == (0, 1) else
                    ('U', (1, 0), lambda y, x: (0, n - x - 1)) if d == (-1, 0) else
                    None)
        if s == 'D':
            return (('B', (-1, 0), lambda y, x: (n - 1, n - x - 1)) if d == (1, 0) else
                    ('L', (-1, 0), lambda y, x: (n - 1, n - y - 1)) if d == (0, -1) else
                    ('R', (-1, 0), lambda y, x: (n - 1, y)) if d == (0, 1) else
                    ('F', (-1, 0), lambda y, x: (n - 1, x)) if d == (-1, 0) else
                    None)

# Real data
cube_coords = {'U': (0, n, 0), 'F': (n, n, 0), 'R': (0, 2 * n, 1), 'L': (2 * n, 0, 1), 'B': (3 * n, 0, 1), 'D': (2 * n, n, 0)}
cube_faces = {x: None for x in cube_coords}
cube_faces['U'] = CubeFace(maze[0][1], 'U')
cube_faces['F'] = CubeFace(maze[1][1], 'F')
cube_faces['R'] = CubeFace(maze[0][2], 'R', 1)
cube_faces['L'] = CubeFace(maze[2][0], 'L', 1)
cube_faces['B'] = CubeFace(maze[3][0], 'B', 1)
cube_faces['D'] = CubeFace(maze[2][1], 'D')

# Test data
#cube_coords = {'U': (0, 2 * n, 0), 'F': (n, 2 * n, 0), 'R': (2 * n, 3 * n, 3), 'L': (n, n, 0), 'B': (n, 0, 0), 'D': (2 * n, 2 * n, 0)}
#cube_faces = {x: None for x in cube_coords}
#cube_faces['U'] = CubeFace(maze[0][2], 'U')
#cube_faces['F'] = CubeFace(maze[1][2], 'F')
#cube_faces['R'] = CubeFace(maze[2][3], 'R', 3)
#cube_faces['L'] = CubeFace(maze[1][1], 'L')
#cube_faces['B'] = CubeFace(maze[1][0], 'B')
#cube_faces['D'] = CubeFace(maze[2][2], 'D')

#for x in cube_faces:
#    print(x)
#    for r in cube_faces[x].data:
#        print(r)
#frontier = []
#idx1 = 0
#idx2 = -1
#for i, t in enumerate(maze[idx1]):
#    if t != None:
#        idx2 = i
#        break
#frontier.append((idx1, idx2, 'U'))
#while len(frontier) > 0:
#    i1, i2, f = frontier.pop(0)
#    if cube_faces[f]:
#        continue
#    cube_faces[f] = (i1, i2)

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

pos = ('U', 0, 0)
d = (0, 1)
for inst in p:
    dy, dx = d
    if inst == 'L':
#        print("Turning left")
#        print()
        d = (-dx, dy)
    elif inst == 'R':
#        print("Turning right")
#        print()
        d = (dx, -dy)
    else:
        f, y, x = pos
#        print("Starting on face", f, "at", (y, x))
#        print()
        c_f = cube_faces[f]
#        for r in c_f.data:
#            print(r)
#        print()
#        print("Moving", inst, "in direction", d)
        last_f, last_y, last_x, last_d = (f, y, x, d)
        for i in range(inst):
            y = y + dy
            x = x + dx
            if y < 0 or y >= n or x < 0 or x >= n:
                new_f, new_d, coord_func = c_f.get_adj_face(d)
                y, x = coord_func(y, x)
                f = new_f
                c_f = cube_faces[f]
#                print("Changing to face", f)
#                print()
#                for r in c_f.data:
#                    print(r)
#                print()
                d = new_d
                dy, dx = d
            if c_f.data[y][x] == '.':
                last_f, last_y, last_x, last_d = (f, y, x, d)
            if c_f.data[y][x] == '#':
                pos = (last_f, last_y, last_x)
                d = last_d
                break
            pos = (f, y, x)
#        print("Ending on face", pos[0], "at", pos[1:])
#        print()

base_y, base_x, rot = cube_coords[pos[0]]
y, x = pos[1:]
for i in range(rot):
    y, x = (n - x - 1, y)
    dy, dx = d
    d = (-dx, dy)
y += base_y + 1
x += base_x + 1
facing = 0 if d == (0, 1) else 1 if d == (1, 0) else 2 if d == (0, -1) else 3
print(1000 * y + 4 * x + facing)
