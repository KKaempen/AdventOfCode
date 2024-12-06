data = []
with open("problem6.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

guard_position = None
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '^':
            guard_position = (i, j)

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

print(len(positions))
