from heapq import heappush, heappop

data = []
with open("problem24.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

width = len(data[1]) - 2
height = len(data) - 2

def gcd(x, y):
    m = min(x, y)
    M = max(x, y)
    while m != 0:
        d = M // m
        temp = M - d * m
        M = m
        m = temp
    return M

def get_storm_poss(storms, storm_poss, c_length, w, h):
    for p in storms:
        y, x = p
        if data[y][x] == '>':
            for c in range(c_length):
                storm_poss[c][y][x - 1] = True
                x = (x % w) + 1
        elif data[y][x] == '<':
            for c in range(c_length):
                storm_poss[c][y][x - 1] = True
                x = ((x - 2) % w) + 1
        elif data[y][x] == 'v':
            for c in range(c_length):
                storm_poss[c][y][x - 1] = True
                y = (y % h) + 1
        elif data[y][x] == '^':
            for c in range(c_length):
                storm_poss[c][y][x - 1] = True
                y = ((y - 2) % h) + 1

cycle_length = (width * height) // gcd(width, height)
storms = [(i, j) for i in range(1, height + 1) for j in range(1, width + 1) if data[i][j] != '.']
storm_poss = [[[False for i in range(width)] for j in range(height + 2)] for k in range(cycle_length)]

get_storm_poss(storms, storm_poss, cycle_length, width, height)
#for a in storm_poss:
#    for r in a:
#        print(''.join([' ' if x else '.' for x in r]))
#    print()

def is_adjacent(p1, p2):
    return (p1[0] == p2[0] and abs(p1[1] - p2[1]) == 1) or (p1[1] == p2[1] and abs(p1[0] - p2[0]) == 1)

def get_actions(p, w, h, s_p, e_p):
    actions = [p]
    y, x = p
    for i in {-1, 1}:
        if y + i >= 1 and y + i <= height and x >= 1 and x <= width:
            actions.append((y + i, x))
        if x + i >= 1 and x + i <= width and y >= 1 and y <= height:
            actions.append((y, x + i))
    if s_p not in actions and is_adjacent(s_p, p):
        actions.append(s_p)
    if e_p not in actions and is_adjacent(e_p, p):
        actions.append(e_p)
    return actions

def get_man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

start_pos = (0, data[0].index('.'))
end_pos = (len(data) - 1, data[-1].index('.'))
start = (0 + get_man_dist(start_pos, end_pos), 0, start_pos, 0)
frontier = [start]
visited = [[[False for i in range(width)] for j in range(height + 2)] for k in range(cycle_length)]
while len(frontier) > 0:
    _, s, p, c = heappop(frontier)
    y, x = p
    if p == end_pos:
        print(s)
        break
    if visited[c][y][x - 1]:
        continue
#    print("Visiting", p, "after", s, "steps on cycle", c)
    visited[c][y][x - 1] = True
    c = (c + 1) % cycle_length
    actions = get_actions(p, width, height, start_pos, end_pos)
    for a in actions:
        if not storm_poss[c][a[0]][a[1] - 1]:
            dist = get_man_dist(a, end_pos)
            heappush(frontier, (s + 1 + dist, s + 1, a, c))

