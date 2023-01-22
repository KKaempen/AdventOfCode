data = open('problem12.txt', 'r').read().splitlines()

right_dict = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
left_dict = {right_dict[v]: v for v in right_dict}
x = 0
y = 0
wx = 10
wy = 1
for da in data:
    inst = da[0]
    am = int(da[1:])
    if inst == 'L':
        inst = 'R'
        am = 360 - am
    if inst == 'R':
        if am == 90:
            temp = wy
            wy = -wx
            wx = temp
        elif am == 180:
            wy = -wy
            wx = -wx
        elif am == 270:
            temp = wy
            wy = wx
            wx = -temp
        continue
    if inst == 'F':
        for i in range(am):
            x += wx
            y += wy

    if inst == 'N':
        wy += am
    elif inst == 'S':
        wy -= am
    elif inst == 'E':
        wx += am
    elif inst == 'W':
        wx -= am

print(abs(x) + abs(y))

