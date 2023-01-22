from copy import deepcopy

data = [[c for c in x] for x in open('problem17.txt', 'r').read().splitlines()]

zerox = 11
zeroy = 11
zeroz = 7
space = [[['.' for i in range(22)] for j in range(22)] for k in range(15)]

for i in range(len(data)):
    for j in range(len(data[0])):
        space[zeroz][zerox + i - 4][zeroy + j - 4] = data[i][j]

def get_num_adjacent(space, x, y, z):
    total = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if not (dx == 0 and dy == 0 and dz == 0):
                    if space[z + dz][x + dx][y + dy] == '#':
                        total += 1
    return total

for i in range(6):
    new_space = deepcopy(space)
    for x in range(1, 21):
        for y in range(1, 21):
            for z in range(1, 14):
                num_adjacent = get_num_adjacent(space, x, y, z)
                if space[z][x][y] == '#' and 2 <= num_adjacent <= 3:
                    new_space[z][x][y] = '#'
                elif space[z][x][y] == '.' and num_adjacent == 3:
                    new_space[z][x][y] = '#'
                else:
                    new_space[z][x][y] = '.'
    space = new_space
                    
count = 0
for x in range(22):
    for y in range(22):
        for z in range(15):
            if space[z][x][y] == '#':
                count += 1

print(count)
