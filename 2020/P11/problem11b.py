data = [[y for y in x] for x in open('problem11.txt', 'r').read().splitlines()]

def is_valid(data, x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0])

def get_good_idxs(data, x, y):
    good_idxs = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
    good_idxs = [d for d in good_idxs if is_valid(data, x + d[0], y + d[1])]
    to_remove = set({})
    real_idxs = {}
    for idx in good_idxs:
        real_idx = idx
        while data[x + real_idx[0]][y + real_idx[1]] == '.':
            real_idx = (real_idx[0] + idx[0], real_idx[1] + idx[1])
            if not is_valid(data, x + real_idx[0], y + real_idx[1]):
                to_remove.add(idx)
                break
        if idx not in to_remove:
            real_idxs[idx] = real_idx
    good_idxs = [real_idxs[idx] for idx in good_idxs if idx not in to_remove]
    return good_idxs

def get_num_occ(data, x, y):
    good_idxs = get_good_idxs(data, x, y)
    num = 0
    for d in good_idxs:
        if data[x + d[0]][y + d[1]] == '#':
            num += 1
    return num

def update_seats(data):
    new_data = [[0 for i in x] for x in data]
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == 'L' and get_num_occ(data, x, y) == 0:
                new_data[x][y] = '#'
            elif data[x][y] == '#' and get_num_occ(data, x, y) >= 5:
                new_data[x][y] = 'L'
            else:
                new_data[x][y] = data[x][y]
    return new_data

while True:
    new_data = update_seats(data)
    if data == new_data:
        break
    data = new_data

print(sum([x.count('#') for x in data]))
