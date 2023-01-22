data = open("problem7.txt", 'r').readlines()[0].strip()
data = sorted([int(x) for x in data.split(',')], reverse = True)

num_crabs = {}

for d in data:
    if d not in num_crabs:
        num_crabs[d] = 0
    num_crabs[d] += 1

locations = sorted([x for x in num_crabs], reverse = True)
best_dist = None
for d in range(max(locations) + 1):
    dist = 0
    for pos in num_crabs:
        delta = abs(pos - d)
        tri_num = (delta * (delta + 1)) // 2
        dist += tri_num * num_crabs[pos]
    if not best_dist or dist < best_dist:
        best_dist = dist

print(best_dist)
