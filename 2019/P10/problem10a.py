data = []
with open("problem10.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

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

def is_closest_asteroid(field, base, aster):
    D_x = aster[0] - base[0]
    D_y = aster[1] - base[1]
    g = gcd(D_x, D_y)
    d_x = D_x // g
    d_y = D_y // g
    idx = 1
    while idx < g:
        if field[base[0] + d_x * idx][base[1] + d_y * idx] == '#':
            break
        idx += 1
    else:
        return True
    return False

best_base = 0
for b in asteroids:
    seen_asters = sum([1 if b != a and is_closest_asteroid(data, b, a) else 0 for a in asteroids])
    best_base = max(seen_asters, best_base)

print(best_base)
