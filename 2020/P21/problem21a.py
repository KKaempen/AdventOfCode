data = open('problem21.txt', 'r').read().splitlines()

data = [(set(d.split(' (contains ')[0].split()), set(d.split(' (contains ')[1][:-1].split(', '))) for d in data]
ingredients = set({})
allergens = set({})
for d in data:
    ingredients |= d[0]
    allergens |= d[1]

eq = {}
for allergen in allergens:
    eq[allergen] = set(ingredients)
    for d in data:
        if allergen in d[1]:
            eq[allergen] &= d[0]

resolved = False
while not resolved:
    resolved = True
    for a in eq:
        if type(eq[a]) == set:
            resolved = False
            if len(eq[a]) == 1:
                (ing,) = eq[a]
                eq[a] = ing
                for b in eq:
                    if a != b and type(eq[b]) == set:
                        try:
                            eq[b].remove(ing)
                        except:
                            continue

bad_ings = set({})
for a in eq:
    bad_ings.add(eq[a])

good = 0
for d in data:
    good += len(d[0] - bad_ings)

print(good)
