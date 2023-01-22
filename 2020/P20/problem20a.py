data = []
with open('problem20.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')

data = '\n'.join(data).split('\n\n')

class Tile:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def get_left(self):
        return ''.join([x[0] for x in self.arr])

    def get_right(self):
        return ''.join([x[self.n - 1] for x in self.arr])

    def get_top(self):
        return ''.join(self.arr[0])

    def get_bottom(self):
        return ''.join(self.arr[self.n - 1]) 

    def get_sides(self):
        return [self.get_left(), self.get_top(), self.get_right(), self.get_bottom()]
        
    def check_compat(self, other):
        self_sides = self.get_sides()
        other_sides = other.get_sides()
        for side in self_sides:
            for other_side in other_sides:
                if side == other_side or side == other_side[::-1]:
                    return True
        return False

tiles = {}
for d in data:
    s = d.split(':\n')
    num = int(s[0].split()[1])
    tiles[num] = Tile([[c for c in x] for x in s[1].split('\n')])

prod = 1
for k in tiles:
    total = 0
    for k2 in tiles:
        if k != k2:
            if tiles[k].check_compat(tiles[k2]):
                total += 1
    if total == 2:
        prod *= k

print(prod)
