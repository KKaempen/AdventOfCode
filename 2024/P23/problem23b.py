from collections import defaultdict

data = []
with open("problem23.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

connections = defaultdict(set)
for line in data:
    n1, n2 = line.split('-')
    connections[n1].add(n2)
    connections[n2].add(n1)

def calc_max_clique(clique, conns, possible):
    if len(possible) == 0:
        return len(clique), clique
    best_val, best_clique = 0, set()
    to_iter = [p for p in possible]
    for p in to_iter:
        new_clique = clique | {p}
        new_possible = conns[p] & possible
        if len(new_clique) + len(new_possible) <= best_val:
            continue
        size, curr_clique = calc_max_clique(new_clique, conns, new_possible)
        possible.remove(p)
        if size > best_val:
            best_val = size
            best_clique = curr_clique
    return best_val, best_clique

_, clique = calc_max_clique(set(), connections, set(connections.keys()))
password = ','.join(sorted([x for x in clique]))
print(password)
