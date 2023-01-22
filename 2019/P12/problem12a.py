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

for k in range(1000):
    update_moons(data)

energy = 0
for m in data:
    p_eng = sum([abs(x) for x in m[0]])
    k_eng = sum([abs(x) for x in m[1]])
    energy += p_eng * k_eng

print(energy)
