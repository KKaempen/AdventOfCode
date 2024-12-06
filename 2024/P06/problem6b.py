data = []
with open("problem6.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[c for c in s] for s in data]

initial_guard_position = None
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '^':
            initial_guard_position = (i, j)

guard_position = initial_guard_position
positions = set()
direc = (-1, 0)
while True:
    x, y = guard_position
    if x < 0 or x >= len(data) or y < 0 or y >= len(data[x]):
        break
    positions.add(guard_position)
    dx, dy = direc
    nx, ny = (x + dx, y + dy)
    while 0 <= nx < len(data) and 0 <= ny < len(data[nx]) and data[nx][ny] == '#':
        dx, dy = (dy, -dx)
        nx, ny = (x + dx, y + dy)
    guard_position = (nx, ny)
    direc = dx, dy

num_obstructions = 0
for i, j in positions:
    if data[i][j] != '.':
        continue
    data[i][j] = '#'
    positions = set()
    direc = (-1, 0)
    guard_position = initial_guard_position
    while True:
        x, y = guard_position
        if x < 0 or x >= len(data) or y < 0 or y >= len(data[x]):
            break
        if (guard_position, direc) in positions:
            num_obstructions += 1
            break
        positions.add((guard_position, direc))
        dx, dy = direc
        nx, ny = (x + dx, y + dy)
        while 0 <= nx < len(data) and 0 <= ny < len(data[nx]) and data[nx][ny] == '#':
            dx, dy = (dy, -dx)
            nx, ny = (x + dx, y + dy)
        guard_position = (nx, ny)
        direc = dx, dy
    data[i][j] = '.'

print(num_obstructions)
