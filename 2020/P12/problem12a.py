data = open('problem12.txt', 'r').read().splitlines()

right_dict = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
left_dict = {right_dict[v]: v for v in right_dict}
x = 0
y = 0
d = 'E'
for da in data:
    inst = da[0]
    am = int(da[1:])
    if inst == 'R':
        turns = am // 90
        for i in range(turns):
            d = right_dict[d]
        continue
    elif inst == 'L':
        turns = am // 90
        for i in range(turns):
            d = left_dict[d]
        continue
    elif inst == 'F':
        inst = d

    if inst == 'N':
        y += am
    elif inst == 'S':
        y -= am
    elif inst == 'E':
        x += am
    elif inst == 'W':
        x -= am

print(abs(x) + abs(y))

