from heapq import heappush, heappop

data = []
with open("problem16.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[c for c in s] for s in data]

start_pos = None
end_pos = None
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == 'S':
            start_pos = (i, j)
        elif c == 'E':
            end_pos = (i, j)

visited = [[[False for _ in line] for line in data] for i in range(4)]
sx, sy = start_pos
frontier = [(0, sx, sy, 0, 1, [(sx, sy)])]
best_dist = 0
best_path = []
while len(frontier) > 0:
    dist, cx, cy, ldx, ldy, path = heappop(frontier)
    dir_idx = 0 if (ldx, ldy) == (0, -1) else 1 if (ldx, ldy) == (0, 1) else 2 if (ldx, ldy) == (-1, 0) else 3
    if visited[dir_idx][cx][cy]:
        continue
    visited[dir_idx][cx][cy] = True
    if (cx, cy) == end_pos:
        best_dist = dist
        best_path = path
        break
    for dx, dy in {(0, -1), (0, 1), (-1, 0), (1, 0)}:
        nx, ny = (cx + dx, cy + dy)
        if data[nx][ny] == '#':
            continue

        if (ldx, ldy) == (dx, dy):
            heappush(frontier, (dist + 1, nx, ny, dx, dy, [p for p in path] + [(nx, ny)]))
        else:
            heappush(frontier, (dist + 1001, nx, ny, dx, dy, [p for p in path] + [(nx, ny)]))

print(best_dist)
