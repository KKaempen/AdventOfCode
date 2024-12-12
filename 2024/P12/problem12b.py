from collections import deque, defaultdict

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
    ver_edges_down = defaultdict(list)
    ver_edges_up = defaultdict(list)
    hor_edges_down = defaultdict(list)
    hor_edges_up = defaultdict(list)

    for cx, cy in region:
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = (cx + dx, cy + dy)
            if (nx, ny) not in region:
                if (dx, dy) == (0, -1):
                    hor_edges_down[cy].append((cx, cx + 1))
                elif (dx, dy) == (0, 1):
                    hor_edges_up[cy + 1].append((cx, cx + 1))
                elif (dx, dy) == (-1, 0):
                    ver_edges_down[cx].append((cy, cy + 1))
                else:
                    ver_edges_up[cx + 1].append((cy, cy + 1))

    edge_groups = [ver_edges_down, ver_edges_up, hor_edges_down, hor_edges_up]
    total_fences = 0
    for group in edge_groups:
        for coord, edges in group.items():
            edges = sorted(edges)
            num_edges = 1
            for i in range(len(edges) - 1):
                curr_edge = edges[i]
                next_edge = edges[i + 1]
                if curr_edge[1] != next_edge[0]:
                    num_edges += 1
            total_fences += num_edges
    
    total += area * total_fences

print(total)

