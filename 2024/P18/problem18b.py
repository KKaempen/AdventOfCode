from collections import deque

data = []
with open("problem18.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [(int(a) for a in x.split(',')) for x in data]

space = [[False for _ in range(71)] for _ in range(71)]
for bx, by in data[:1024]:
    space[bx][by] = True

for bx, by in data[1024:]:
    space[bx][by] = True
    frontier = deque()
    frontier.append((0, 0, 0))
    best_len = 0
    visited = [[False for _ in range(71)] for _ in range(71)]
    while len(frontier) > 0:
        dist, fx, fy = frontier.popleft()
        if visited[fx][fy]:
            continue
        visited[fx][fy] = True
        if (fx, fy) == (70, 70):
            best_len = dist
            break
        for dx, dy in {(0, -1), (0, 1), (-1, 0), (1, 0)}:
            nx, ny = (fx + dx, fy + dy)
            if 0 <= nx < len(space) and 0 <= ny < len(space[nx]) and not space[nx][ny]:
                frontier.append((dist + 1, nx, ny))
    if best_len == 0:
        print((bx, by))
        break
