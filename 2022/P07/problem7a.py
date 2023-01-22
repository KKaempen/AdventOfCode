data = []
with open("problem7.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

class DirNode:
    def __init__(self):
        self.dirs = {}
        self.files = []
        self.parent = None

root = DirNode()
curr = root
for d in data:
    if d[0] == '$':
        d = d[2:]
        if d[0:2] == 'cd':
            dest = d[3:]
            if dest == '/':
                curr = root
            elif dest == '..':
                curr = curr.parent
            else:
                dirs = curr.dirs
                if dest not in dirs:
                    new = DirNode()
                    new.parent = curr
                    dirs[dest] = new
                curr = dirs[dest]
        elif d[0:2] == 'ls':
            pass
    else:
        if d[0:3] == 'dir':
            dest = d[4:]
            dirs = curr.dirs
            if dest not in dirs:
                new = DirNode()
                new.parent = curr
                dirs[dest] = new
        else:
            f = d.split(' ')
            size = int(f[0])
            name = f[1]
            curr.files.append((size, name))

def get_dir_totals(node):
    file_total = sum([t[0] for t in node.files])
    dir_totals, running_sum = (0, 0)
    for name in node.dirs:
        d = node.dirs[name]
        new_total, new_running_sum = get_dir_totals(d)
        dir_totals += new_total
        running_sum += new_running_sum
    total_size = file_total + dir_totals
    if total_size <= 100000:
        running_sum += total_size
    return total_size, running_sum

t, answer = get_dir_totals(root)
print(answer)

