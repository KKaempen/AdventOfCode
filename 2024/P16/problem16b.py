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

visited = [[[-1 for _ in line] for line in data] for i in range(4)]
preds = [[[set() for _ in line] for line in data] for i in range(4)]
sx, sy = start_pos
frontier = [(0, sx, sy, 0, 1, -1, 0, 0)]
while len(frontier) > 0:
    dist, cx, cy, ldx, ldy, pdidx, px, py = heappop(frontier)
    dir_idx = 0 if (ldx, ldy) == (0, -1) else 1 if (ldx, ldy) == (0, 1) else 2 if (ldx, ldy) == (-1, 0) else 3
    if visited[dir_idx][cx][cy] < 0:
        visited[dir_idx][cx][cy] = dist
    if dist > visited[dir_idx][cx][cy]:
        continue

    preds[dir_idx][cx][cy] |= preds[pdidx][px][py]
    if pdidx >= 0:
        preds[dir_idx][cx][cy].add((px, py))

    for dx, dy in {(0, -1), (0, 1), (-1, 0), (1, 0)}:
        nx, ny = (cx + dx, cy + dy)
        if data[nx][ny] == '#':
            continue

        if (ldx, ldy) == (dx, dy):
            heappush(frontier, (dist + 1, nx, ny, dx, dy, dir_idx, cx, cy))
        else:
            heappush(frontier, (dist + 1001, nx, ny, dx, dy, dir_idx, cx, cy))

best_dist = 1000 * len(data) * len(data[0])
for i in range(4):
    if visited[i][end_pos[0]][end_pos[1]] >= 0:
        best_dist = min(best_dist, visited[i][end_pos[0]][end_pos[1]])

all_visited = {end_pos}
for i in range(4):
    if visited[i][end_pos[0]][end_pos[1]] == best_dist:
        all_visited |= preds[i][end_pos[0]][end_pos[1]]

print(len(all_visited))
