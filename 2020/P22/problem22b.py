data = open('problem22.txt', 'r').read().splitlines()

b = data.index('')
d1 = data[1:b]
d2 = data[b + 2:]
d1 = tuple([int(x) for x in d1])
d2 = tuple([int(x) for x in d2])

def recursive_combat(d1, d2):
    seen = set({})
    while len(d1) != 0 and len(d2) != 0:
        if (d1, d2) in seen:
            return (1, d1)
        seen.add((d1, d2))
        c1 = d1[0]
        c2 = d2[0]
        d1 = d1[1:]
        d2 = d2[1:]
        wins = -1
        if len(d1) >= c1 and len(d2) >= c2:
            wins, vals = recursive_combat(d1[:c1], d2[:c2])
        else:
            if c1 > c2:
                wins = 1
            else:
                wins = 2
        if wins == 1:
            d1 += (c1, c2)
        elif wins == 2:
            d2 += (c2, c1)
        else:
            print("Fuck")
    return (1, d1) if len(d2) == 0 else (2, d2)

wins, winner = recursive_combat(d1, d2)
score = 0
for i, c in enumerate(winner):
    score += c * (len(winner) - i)

print(score)
