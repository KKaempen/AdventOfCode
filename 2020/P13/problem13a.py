f = open('problem13.txt', 'r').read().splitlines()

t = int(f[0])
ids = [int(x) for x in f[1].split(',') if x != 'x']

best = None
best_time = -1
for idx in ids:
    if best == None or (t // idx + 1) * idx - t < best_time:
        best = idx
        best_time = (t // idx + 1) * idx - t
print(best * best_time)
