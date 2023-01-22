from functools import cmp_to_key

data = []
with open("problem10.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[y for y in x] for x in data]

asteroids = [(x, y) for x in range(len(data)) for y in range(len(data[x])) if data[x][y] == '#']

def gcd(x, y):
    x = abs(x)
    y = abs(y)
    m = min(x, y)
    M = max(x, y)
    while m != 0:
        div = M // m
        temp = M - m * div
        M = m
        m = temp
    return M

def get_direc(base, point):
    D_x = point[0] - base[0]
    D_y = point[1] - base[1]
    g = gcd(D_x, D_y)
    return (D_x // g, D_y // g)

def get_closest_asteroid(field, base, direc):
    d_x, d_y = direc
    p_x = base[0] + d_x
    p_y = base[1] + d_y
    while (
        p_x < len(field) and
        p_x >= 0 and
        p_y < len(field[0]) and
        p_y >= 0
        ):
        if field[p_x][p_y] == '#':
            return (p_x, p_y)
        p_x += d_x
        p_y += d_y
    return None

def rot_comp(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    q1 = (
        1 if x1 < 0 and y1 >= 0 else
        2 if x1 >= 0 and y1 > 0 else
        3 if x1 > 0 and y1 <= 0 else
        4 if x1 <= 0 and y1 < 0 else
        None
    )
    q2 = (
        1 if x2 < 0 and y2 >= 0 else
        2 if x2 >= 0 and y2 > 0 else
        3 if x2 > 0 and y2 <= 0 else
        4 if x2 <= 0 and y2 < 0 else
        None
    )
    if q1 < q2:
        return -1
    elif q1 > q2:
        return 1
    if q1 == 1 or q1 == 3:
        d1 = y1 / x1
        d2 = y2 / x2
        if d1 > d2:
            return -1
        elif d1 < d2:
            return 1
        elif d1 == d2:
            return 0
    elif q1 == 2 or q1 == 4:
        d1 = x1 / y1
        d2 = x2 / y2
        if d1 < d2:
            return -1
        elif d1 > d2:
            return 1
        elif d1 == d2:
            return 0

station_loc = (20, 23)

direcs = [y for y in {get_direc(station_loc, x) for x in asteroids if x != station_loc}]
direcs = sorted(direcs, key=cmp_to_key(rot_comp))

num_destroyed = 0
while len(direcs) > 0:
    bad_idxs = set({})
    for i, d in enumerate(direcs):
        a = get_closest_asteroid(data, station_loc, d)
        if a:
            data[a[0]][a[1]] = '.'
            num_destroyed += 1
#            print("In direction", d)
#            print("Asteroid number", num_destroyed, "destroyed:", a[1], ",", a[0])
#            input()
            if num_destroyed == 200:
                print(a[1] * 100 + a[0])
                direcs = []
                break
        else:
            bad_idxs.add(i)
    direcs = [x for i, x in enumerate(direcs) if i not in bad_idxs]
