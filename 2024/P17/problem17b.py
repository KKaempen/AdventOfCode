data = []
with open("problem17.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

ops_str = data[-1]
ops = [int(x) for x in ops_str[9:].split(',')]

patterns = [[None for _ in range(8)] for _ in range(8)]
for op in range(8):
    for last_three in range(8):
        shift = last_three ^ 7
        c = last_three ^ op
        a = [last_three & 1, (last_three & 2) >> 1, (last_three & 4) >> 2]
        while len(a) < shift + 3:
            a.append(-1)
        for i in range(3):
            mask = 1 if i == 0 else 2 if i == 1 else 4
            to_place = (c & mask) >> i
            idx = i + shift
            if a[idx] >= 0 and a[idx] != to_place:
                break
            a[idx] = to_place
        else:
            patterns[op][last_three] = a

possible_as = [[]]
for i, op in enumerate(ops):
    new_possible = []
    shift = i * 3
    next_chunks = patterns[op]
    for a in possible_as:
        for chunk in next_chunks:
            if chunk is None:
                continue
            new_a = [x for x in a]
            while len(new_a) < shift + len(chunk):
                new_a.append(-1)
            for i, v in enumerate(chunk):
                if new_a[i + shift] >= 0 and chunk[i] >= 0 and new_a[i + shift] != chunk[i]:
                    break
                new_a[i + shift] = max(new_a[i + shift], chunk[i])
            else:
                new_possible.append(new_a)
    possible_as = new_possible

best_a = possible_as[0]
total = 0
for v in best_a[::-1]:
    total *= 2
    total += v
print(total)
