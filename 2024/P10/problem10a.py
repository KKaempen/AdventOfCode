from collections import deque

data = []
with open("problem10.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

possible_trailheads = set()
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == '0':
            possible_trailheads.add((i, j))

count = 0
for tx, ty in possible_trailheads:
    frontier = deque()
    frontier.append((tx, ty))
    reachable = set()
    visited = [[False for c in line] for line in data]
    while len(frontier) > 0:
        cx, cy = frontier.popleft()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        if data[cx][cy] == '9':
            reachable.add((cx, cy))
        else:
            val = int(data[cx][cy])
            next_val = str(val + 1)
            for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                nx, ny = (cx + dx, cy + dy)
                if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[nx]):
                    continue
                if data[nx][ny] == next_val:
                    frontier.append((nx, ny))
    count += len(reachable)

print(count)

