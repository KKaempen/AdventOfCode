data = open("problem7.txt", 'r').readlines()[0].strip()
data = sorted([int(x) for x in data.split(',')], reverse = True)

num_crabs = {}

for d in data:
    if d not in num_crabs:
        num_crabs[d] = 0
    num_crabs[d] += 1

locations = sorted([x for x in num_crabs], reverse = True)
best_dist = sum(data)
for d in locations:
    dist = 0
    for pos in num_crabs:
        dist += abs(pos - d) * num_crabs[pos]
    if dist < best_dist:
        best_dist = dist

print(best_dist)
