data = []
with open("example.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

line = [(int(c), i // 2) if i % 2 == 0 else (int(c), None) for i, c in enumerate(data[0])]
arr = []

idx = len(line) - 1
while idx > 0:
    count, val = line[idx]
    if val is None:
        idx -= 1
        continue
    for i in range(idx):
        if line[i][1] is not None or line[i][0] < count:
            continue
        line[i] = (line[i][0] - count, line[i][1])
        line[idx] = (count, None)
        line.insert(i, (count, val))
        idx += 1
        break
    idx -= 1

total = 0
curr_idx = 0
for (count, val) in line:
    if val is None:
        curr_idx += count
        continue
    for i in range(count):
        total += curr_idx * val
        curr_idx += 1

print(total)
