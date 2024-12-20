from collections import deque, defaultdict

data = []
with open("problem20.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[c for c in line] for line in data]

start_pos = None
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == 'S':
            start_pos = (i, j)

best_time = 0
frontier = deque()
frontier.append((0, start_pos[0], start_pos[1]))
visited = [[False for _ in line] for line in data]
shortest_paths = [[-1 for _ in line] for line in data]
while len(frontier) > 0:
    dist, cx, cy = frontier.popleft()
    if visited[cx][cy]:
        continue
    visited[cx][cy] = True
    shortest_paths[cx][cy] = dist
    if data[cx][cy] == 'E':
        best_time = dist
        break
    for dx, dy in {(0, -1), (0, 1), (-1, 0), (1, 0)}:
        nx, ny = (cx + dx, cy + dy)
        if data[nx][ny] == '#':
            continue
        frontier.append((dist + 1, nx, ny))

count = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if shortest_paths[i][j] == -1:
            continue
        start_dist1 = shortest_paths[i][j]
        mincx, mincy = (max(1, i - 20), max(1, j - 20))
        maxcx, maxcy = (min(len(data) - 2, i + 20), min(len(data[i]) - 2, j + 20))
        for cx in range(mincx, maxcx + 1):
            for cy in range(mincy, maxcy + 1):
                start_dist2 = shortest_paths[cx][cy]
                dist = abs(cx - i) + abs(cy - j)
                if (
                    data[cx][cy] != '#' and
                    dist <= 20 and
                    start_dist2 - start_dist1 - dist >= 100
                ):
                    count += 1

print(count)
