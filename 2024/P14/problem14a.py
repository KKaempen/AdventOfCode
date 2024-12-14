data = []
with open("problem14.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

q1, q2, q3, q4 = (0, 0, 0, 0)
hx = 50
hy = 51
for line in data:
    p_str, v_str = line.split()
    px, py = [int(x) for x in p_str[2:].split(',')]
    vx, vy = [int(x) for x in v_str[2:].split(',')]

    fx, fy = (px + vx * 100, py + vy * 100)
    if fx < 0:
        dx = fx // 101
        fx -= dx * 101
        if fx < 0:
            fx += 101
    if fy < 0:
        dy = fy // 103
        fy -= dy * 103
        if fy < 0:
            fy += 103
    fx = fx % 101
    fy = fy % 103
    if fx < hx and fy < hy:
        q1 += 1
    elif fx < hx and fy > hy:
        q2 += 1
    elif fx > hx and fy < hy:
        q3 += 1
    elif fx > hx and fy > hy:
        q4 += 1

print(q1 * q2 * q3 * q4)
    
