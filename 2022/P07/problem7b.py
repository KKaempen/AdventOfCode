data = []
with open("problem7.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

class DirNode:
    def __init__(self, name):
        self.dirs = {}
        self.files = []
        self.parent = None
        self.name = name

root = DirNode('/')
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
                    new = DirNode(dest)
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
                new = DirNode(dest)
                new.parent = curr
                dirs[dest] = new
        else:
            f = d.split(' ')
            size = int(f[0])
            name = f[1]
            curr.files.append((size, name))

large_dirs = []

def get_dir_totals(node):
    file_total = sum([t[0] for t in node.files])
    dir_totals = 0
    for name in node.dirs:
        d = node.dirs[name]
        dir_totals += get_dir_totals(d)
    total_size = file_total + dir_totals
    return total_size

overall_size = get_dir_totals(root)
need_to_delete = overall_size - 40000000

def get_dir_totals_2(node):
    file_total = sum([t[0] for t in node.files])
    dir_totals = 0
    for name in node.dirs:
        d = node.dirs[name]
        dir_totals += get_dir_totals_2(d)
    total_size = file_total + dir_totals
    if total_size >= need_to_delete:
        large_dirs.append((total_size, node.name))
    return total_size

get_dir_totals_2(root)
optimal = min(large_dirs)

print(optimal[0])

