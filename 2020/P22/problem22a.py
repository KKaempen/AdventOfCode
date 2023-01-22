data = open('problem22.txt', 'r').read().splitlines()

b = data.index('')
d1 = data[1:b]
d2 = data[b + 2:]
d1 = [int(x) for x in d1]
d2 = [int(x) for x in d2]

while len(d1) != 0 and len(d2) != 0:
    c1 = d1[0]
    c2 = d2[0]
    d1 = d1[1:]
    d2 = d2[1:]
    if c1 > c2:
        d1 += [c1, c2]
    else:
        d2 += [c2, c1]

winner = d1 if len(d2) == 0 else d2
score = 0
for i, c in enumerate(winner):
    score += c * (len(winner) - i)

print(score)
