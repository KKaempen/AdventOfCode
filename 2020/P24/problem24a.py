data = []
with open('problem24.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')

def get_coords(s):
    x, y = (0, 0)
    i = 0
    while i < len(s):
        d = s[i]
        if d in {'s', 'n'}:
            d = s[i:i + 2]
            i += 1
        i += 1
        if d == 'e':
            x += 1
        elif d == 'w':
            x -= 1
        elif d == 'ne':
            y += 1
            x += 1
        elif d == 'nw':
            y += 1
        elif d == 'se':
            y -= 1
        elif d == 'sw':
            y -= 1
            x -= 1
    return x, y

flip_dict = {'black': 'white', 'white': 'black'}
tiles = {}
for d in data:
    t = get_coords(d)
    if t in tiles:
        tiles[t] = flip_dict[tiles[t]]
    else:
        tiles[t] = 'black'

total = 0
for t in tiles:
    if tiles[t] == 'black':
        total += 1

print(total)
