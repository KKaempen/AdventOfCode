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

def get_adj(t):
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y - 1)]

def add_all_adj(tile_dict):
    all_adj = [p for t in tile_dict for p in get_adj(t)]
    for t in all_adj:
        if t in tile_dict:
            continue
        tile_dict[t] = 'white'

flip_dict = {'black': 'white', 'white': 'black'}
tiles = {}
for d in data:
    t = get_coords(d)
    if t in tiles:
        tiles[t] = flip_dict[tiles[t]]
    else:
        tiles[t] = 'black'

for i in range(100):
    add_all_adj(tiles)
    to_flip = []
    for t in tiles:
        adj = get_adj(t)
        count = 0
        if tiles[t] == 'black':
            for a in adj:
                if tiles[a] == 'black':
                    count += 1
            if count < 1 or count > 2:
                to_flip.append(t)
        elif tiles[t] == 'white':
            for a in (a for a in adj if a in tiles):
                if tiles[a] == 'black':
                    count += 1
            if count == 2:
                to_flip.append(t)
    for t in to_flip:
        tiles[t] = flip_dict[tiles[t]]

print(len([tiles[t] for t in tiles if tiles[t] == 'black']))
