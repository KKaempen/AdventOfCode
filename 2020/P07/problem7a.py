data = open('problem7.txt', 'r').read().splitlines()

rules = {}
for d in data:
    x = d[:-1].split(' contain ')
    c_color = x[0][:-5]
    for b in x[1].split(', '):
        if b != 'no other bags':
            color = ' '.join(b.split(' ')[1:-1])
            if color not in rules:
                rules[color] = set({})
            rules[color].add(c_color)

colors = {'shiny gold'}
added = True
while added:
    added = False
    l = len(colors)
    for color in colors:
        if color in rules:
            colors = colors | rules[color]
    if len(colors) > l:
        added = True

print(len(colors) - 1)
