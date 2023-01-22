data = open('problem8.txt', 'r').read().splitlines()

used_idx = set({})
acc = 0
idx = 0
not_looping = True
while not_looping:
    d = data[idx].split()
    used_idx.add(idx)
    if d[0] == 'nop':
        idx += 1
    elif d[0] == 'acc':
        acc += int(d[1])
        idx += 1
    elif d[0] == 'jmp':
        idx += int(d[1])
    if idx in used_idx:
        not_looping = False

print(acc)
