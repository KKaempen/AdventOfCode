data = []
with open('problem20.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')

data = '\n'.join(data).split('\n\n')

sea_monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
sea_monster = [[c for c in s] for s in sea_monster.strip('\n').split('\n')] 

class Tile:
    def __init__(self, arr):
        self.arr = arr

    def print(self):
        for x in self.arr:
            print(''.join(x))
        print()

    def flip_x(self):
        for i in range(len(self.arr)):
            self.arr[i] = self.arr[i][::-1]

    def flip_y(self):
        self.arr = self.arr[::-1]

    def flip_diag(self):
        a = self.arr
        self.arr = [[x[i] for x in a] for i in range(len(a[0]))]

    def get_left(self):
        return ''.join([x[0] for x in self.arr])

    def get_right(self):
        return ''.join([x[len(self.arr) - 1] for x in self.arr])

    def get_top(self):
        return ''.join(self.arr[0])

    def get_bottom(self):
        return ''.join(self.arr[len(self.arr) - 1]) 

    def get_sides(self):
        return [self.get_left(), self.get_top(), self.get_right(), self.get_bottom()]

    def matches_side(self, other_side):
        for i, side in enumerate(self.get_sides()):
            if side == other_side:
                return i + 1
            elif side == other_side[::-1]:
                return -i - 1
        return None

    def is_right_neighbor(self, other_side):
        res = self.matches_side(other_side)
        if not res:
            return False
        res_val = abs(res)
        if res_val == 2 or res_val == 4:
            self.flip_diag()
        if res_val == 3 or res_val == 4:
            self.flip_x() 
        if res < 0:
            self.flip_y()
        return True

    def is_bottom_neighbor(self, other_side):
        res = self.matches_side(other_side)
        if not res:
            return False
        res_val = abs(res)
        if res_val == 1 or res_val == 3:
            self.flip_diag()
        if res_val == 3 or res_val == 4:
            self.flip_y()
        if res < 0:
            self.flip_x()
        return True
        
    def check_compat(self, other):
        for j, other_side in enumerate(other.get_sides()):
            res = self.matches_side(other_side)
            if res:
                return (j + 1, res)
        return None

    def remove_border(self):
        self.arr = [x[1:-1] for x in self.arr[1:-1]]

    def join_right(self, other):
        for i in range(len(self.arr)):
            self.arr[i] += other.arr[i]
        other.arr = []

    def join_bottom(self, other):
        self.arr += other.arr
        other.arr = []

    def find_pattern(self, s):
        a = self.arr
        for i in range(len(a) - len(s) + 1):
            for j in range(len(a[0]) - len(s[0]) + 1):
                failed = False
                for k in range(len(s)):
                    for l in range(len(s[0])):
                        if s[k][l] == ' ':
                            continue
                        if s[k][l] != a[i + k][j + l]:
                            failed = True
                    if failed:
                        break
                if not failed:
                    return (i, j)
        return None

    def replace_pattern(self, s, loc):
        for i in range(len(s)):
            for j in range(len(s[0])):
                if s[i][j] == ' ':
                    continue
                self.arr[loc[0] + i][loc[1] + j] = 'O'
        
    def adjust_for_pattern(self, s):
        for i in {-1, 1}:
            for j in {-1, 1}:
                for k in {-1, 1}:
                    if i < 0:
                        self.flip_diag()
                    if j < 0:
                        self.flip_y()
                    if k < 0:
                        self.flip_x()
                    if self.find_pattern(s):
                        return True
                    if k < 0:
                        self.flip_x()
                    if j < 0:
                        self.flip_y()
                    if i < 0:
                        self.flip_diag()
        return False
        

tiles = {}
for d in data:
    s = d.split(':\n')
    num = int(s[0].split()[1])
    tiles[num] = Tile([[c for c in x] for x in s[1].split('\n')])

corner_tiles = []
for k in tiles:
    total = 0
    for k2 in tiles:
        if k != k2:
            if tiles[k].check_compat(tiles[k2]):
                total += 1
    if total == 2:
        corner_tiles.append(k)

ordered_tiles = []
row = []
row.append(corner_tiles[0])
for k in tiles:
    t1 = tiles[row[0]]
    t2 = tiles[k]
    p = t1.check_compat(t2)
    if not p:
        continue
    if abs(p[1]) == 1:
        t1.flip_x()
    if abs(p[1]) == 2:
        t1.flip_y()

curr_idx = 0
while curr_idx >= 0:
    right_side = tiles[row[curr_idx]].get_right()
    for k in tiles:
        if k == row[curr_idx]:
            continue
        t = tiles[k]
        if t.is_right_neighbor(right_side):
            row.append(k)
            curr_idx += 1
            if k in corner_tiles:
                curr_idx = -1
            break

ordered_tiles.append(row.copy())
curr_idx = 0
while curr_idx >= 0:
    row = []
    for i in range(len(ordered_tiles[curr_idx])):
        last_tile_idx = ordered_tiles[curr_idx][i]
        last_tile = tiles[last_tile_idx]
        bottom_side = last_tile.get_bottom()
        for k in tiles:
            if k == last_tile_idx:
                continue
            t = tiles[k]
            if t.is_bottom_neighbor(bottom_side):
                row.append(k)
                break
    ordered_tiles.append(row.copy())
    curr_idx += 1
    if row[0] in corner_tiles:
        curr_idx = -1

ordered_tiles = [[tiles[k] for k in x] for x in ordered_tiles]
tile_rows = []
for r in ordered_tiles:
    t = r[0]
    t.remove_border()
    for t2 in r[1:]:
        t2.remove_border()
        t.join_right(t2)
    tile_rows.append(t)

t = tile_rows[0]
for t2 in tile_rows[1:]:
    t.join_bottom(t2)

t.adjust_for_pattern(sea_monster)
while p := t.find_pattern(sea_monster):
    t.replace_pattern(sea_monster, p)
print(sum([r.count('#') for r in t.arr]))
