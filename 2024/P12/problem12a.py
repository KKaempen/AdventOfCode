from collections import deque

data = []
with open("problem12.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

regions = []
counted = set()
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if (i, j) in counted:
            continue
        base_char = c
        frontier = deque()
        frontier.append((i, j))
        new_region = set()
        visited = [[False for _ in temp] for temp in data]
        while len(frontier) > 0:
            cx, cy = frontier.popleft()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            if data[cx][cy] != base_char:
                continue
            counted.add((cx, cy))
            new_region.add((cx, cy))
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = (cx + dx, cy + dy)
                if 0 <= nx < len(data) and 0 <= ny < len(data[nx]):
                    frontier.append((nx, ny))
        regions.append(new_region)

total = 0
for region in regions:
    area = len(region)
    perimeter = 0
    for cx, cy in region:
        to_add = 4
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = (cx + dx, cy + dy)
            if (nx, ny) in region:
                to_add -= 1
        perimeter += to_add
    total += area * perimeter

print(total)

