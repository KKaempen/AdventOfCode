cups = open('problem23.txt', 'r').read().splitlines()[0]

n = len(cups)

cur = 0
for i in range(100):
    cur_lab = cups[cur]
    dest = (int(cups[cur]) - 2) % n + 1
    next_3 = cups[cur + 1:cur + 4]
    if len(next_3) < 3:
        next_3 += cups[:(cur + 4) % n]
    for c in next_3:
        cups = cups.replace(c, '')
    while str(dest) in next_3:
        dest = (dest - 2) % n + 1
    dest = str(dest)
    idx = cups.find(dest)
    cups = cups[:idx + 1] + next_3 + cups[idx + 1:]
    cur = (cups.find(cur_lab) + 1) % n

one_idx = cups.find('1')
print(cups[one_idx + 1:] + cups[:one_idx])
