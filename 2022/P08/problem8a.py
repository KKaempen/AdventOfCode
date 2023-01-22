data = []
with open("problem8.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[int(x) for x in s] for s in data]
n = len(data)
seen = [[False for i in range(n)] for j in range(n)]

last_seen_left = -1
last_seen_right = -1
last_seen_top = -1
last_seen_bottom = -1
for i in range(n):
    last_seen_left = -1
    last_seen_right = -1
    last_seen_top = -1
    last_seen_bottom = -1
    for j in range(n):
        if data[i][j] > last_seen_left:
            last_seen_left = data[i][j]
            seen[i][j] = True
        if data[i][n - j - 1] > last_seen_right:
            last_seen_right = data[i][n - j - 1]
            seen[i][n - j - 1] = True
        if data[j][i] > last_seen_top:
            last_seen_top = data[j][i]
            seen[j][i] = True
        if data[n - j - 1][i] > last_seen_bottom:
            last_seen_bottom = data[n - j - 1][i]
            seen[n - j - 1][i] = True

print(sum([sum([1 if x else 0 for x in a]) for a in seen]))

