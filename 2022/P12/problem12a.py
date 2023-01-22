from string import ascii_lowercase
from heapq import heappush, heappop
char_map = {ascii_lowercase[i]: i for i in range(26)}

data = []
with open("problem12.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[x for x in s] for s in data]

start_pos = None
end_pos = None
for i, a in enumerate(data):
    if 'S' in a:
        j = a.index('S')
        start_pos = (i, j)
    if 'E' in a:
        j = a.index('E')
        end_pos = (i, j)

data[start_pos[0]][start_pos[1]] = 'a'
data[end_pos[0]][end_pos[1]] = 'z'
data = [[char_map[c] for c in a] for a in data]

visited = [[None for x in a] for a in data]
x_max = len(data)
y_max = len(data[0])

def get_valid_adj(p, x_max, y_max):
    x = p[0]
    y = p[1]
    adj = []
    if x + 1 < x_max:
        adj.append((x + 1, y))#, 'v'))
    if x - 1 >= 0:
        adj.append((x - 1, y))#, '^'))
    if y + 1 < y_max:
        adj.append((x, y + 1))#, '>'))
    if y - 1 >= 0:
        adj.append((x, y - 1))#, '<'))
    return adj

frontier = [(0, start_pos)]
while len(frontier) > 0:
    p = heappop(frontier)
    dist = p[0]
    loc = p[1]
    if visited[loc[0]][loc[1]]:
        continue
    visited[loc[0]][loc[1]] = dist
    adj = get_valid_adj(loc, x_max, y_max)
    for a in adj:
        if data[a[0]][a[1]] - data[loc[0]][loc[1]] > 1:
            continue
        heappush(frontier, (dist + 1, a))

print(visited[end_pos[0]][end_pos[1]])

