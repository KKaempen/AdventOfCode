from re import match

data = []
with open("problem12.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

r = r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>'
data = [[int(x) for x in match(r, s).groups()] for s in data]
data = [[tuple(x), (0, 0, 0)] for x in data]

def update_vels(p1, p2, v1, v2): 
    dx = 1 if p1[0] < p2[0] else -1 if p1[0] > p2[0] else 0
    dy = 1 if p1[1] < p2[1] else -1 if p1[1] > p2[1] else 0
    dz = 1 if p1[2] < p2[2] else -1 if p1[2] > p2[2] else 0 
    v1_new = (v1[0] + dx, v1[1] + dy, v1[2] + dz) 
    v2_new = (v2[0] - dx, v2[1] - dy, v2[2] - dz)
    return v1_new, v2_new

def update_pos(p, v):
    return (p[0] + v[0], p[1] + v[1], p[2] + v[2])

def update_moons(moons):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            m1 = data[i]
            m2 = data[j]
            m1[1], m2[1] = update_vels(m1[0], m2[0], m1[1], m2[1])
    for m in data:
        m[0] = update_pos(m[0], m[1]) 

def gcd(x, y):
    while y > 0:
        x, y = (y, x % y)
    return x

start_data = [x.copy() for x in data]
repeats = [0, 0, 0]
count = 0
while True:
    update_moons(data)
    count += 1
    for i in range(3):
        start_coords = [[x[0][i], x[1][i]] for x in start_data]
        curr_coords = [[x[0][i], x[1][i]] for x in data]
        if repeats[i] == 0 and start_coords == curr_coords:
            repeats[i] = count
    is_zero = 0 in repeats
    if not is_zero:
        break

num = 1
for x in repeats:
    g = gcd(num, x)
    num *= x
    num //= g
print(num)
