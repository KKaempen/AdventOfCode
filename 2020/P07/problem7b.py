data = open('problem7.txt', 'r').read().splitlines()

rules = {}
for d in data:
    x = d[:-1].split(' contain ')
    c_color = x[0][:-5]
    for b in x[1].split(', '):
        if b != 'no other bags':
            color = ' '.join(b.split(' ')[1:-1])
            num = int(b.split(' ')[0])
            if c_color not in rules:
                rules[c_color] = set({})
            rules[c_color].add((color, num))
        else:
            rules[c_color] = set({})

def add_colors(color):
    total = 0
    for o_color, num in rules[color]:
        total += num * (1 + add_colors(o_color))
    return total

print(add_colors('shiny gold'))
