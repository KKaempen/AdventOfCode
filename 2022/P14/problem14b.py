data = []
with open("problem14.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[(int(x.split(',')[0]), int(x.split(',')[1])) for x in a.split(' -> ')] for a in data]
max_y = max([x[1] for a in data for x in a]) + 2
min_x = min(min([x[0] for a in data for x in a]), 500 - max_y)
max_x = max(max([x[0] for a in data for x in a]), 500 + max_y)
area = [['.' for i in range(max_x - min_x + 1)] for j in range(max_y + 1)]
area[-1] = ['#' for i in range(max_x - min_x + 1)]

def draw_line(path, a, m_x):
    for i in range(len(path) - 1):
        s = path[i]
        f = path[i + 1]
        x_s = s[0] - m_x
        x_f = f[0] - m_x
        y_s = s[1]
        y_f = f[1]
        if x_s != x_f:
            for i in range(min(x_s, x_f), max(x_s, x_f) + 1):
                a[y_s][i] = '#'
        elif y_s != y_f:
            for i in range(min(y_s, y_f), max(y_s, y_f) + 1):
                a[i][x_s] = '#'

def can_move(grain, a):
    gx = grain[0]
    gy = grain[1]
    if gy + 1 >= len(a) or a[gy + 1][gx] == '.':
        return (gx, gy + 1)
    elif gx - 1 < 0 or a[gy + 1][gx - 1] == '.':
        return (gx - 1, gy + 1)
    elif gx + 1 >= len(a[gy + 1]) or a[gy + 1][gx + 1] == '.':
        return (gx + 1, gy + 1)
    else:
        return None

for d in data:
    draw_line(d, area, min_x)

num_grains = 0
while True:
    grain_pos = (500 - min_x, 0)
    if not can_move(grain_pos, area):
        num_grains += 1
        break
    while new_grain_pos := can_move(grain_pos, area):
        grain_pos = new_grain_pos
    area[grain_pos[1]][grain_pos[0]] = 'o'
    num_grains += 1

print(num_grains)
    
