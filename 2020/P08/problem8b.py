data = open('problem8.txt', 'r').read().splitlines()

def will_loop(data):
    used_idx = set({})
    acc = 0
    idx = 0
    not_looping = True

    while not_looping and idx < len(data):
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

    if not_looping:
        return acc
    else:
        return None

for i in range(len(data)):
    if data[i].split()[0] == 'nop':
        data2 = list(data)
        data2[i] = 'jmp' + data2[i][3:]
        r = will_loop(data)
        if r:
            print(r)
            break
    elif data[i].split()[0] == 'jmp':
        data2 = list(data)
        data2[i] = 'nop' + data2[i][3:]
        r = will_loop(data2)
        if r:
            print(r)
            break
