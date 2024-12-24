from collections import defaultdict, deque

data = []
with open("problem24.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

inits, rules = '\n'.join(data).split('\n\n')
graph = {}
all_ps = set()
for rule in rules.split('\n'):
    preds, term = rule.split(' -> ')
    p1, p2, rule = (None, None, None)
    if 'XOR' in preds:
        p1, p2 = preds.split(' XOR ')
        rule = lambda x, y: x ^ y
    elif 'OR' in preds:
        p1, p2 = preds.split(' OR ')
        rule = lambda x, y: x | y
    elif 'AND' in preds:
        p1, p2 = preds.split(' AND ')
        rule = lambda x, y: x & y
    all_ps.add(term)
    all_ps.add(p1)
    all_ps.add(p2)
    graph[term] = (p1, p2, rule)

vals = {}
for init in inits.split('\n'):
    detail, val = init.split(': ')
    int_val = int(val)
    vals[detail] = int_val

in_edges = defaultdict(set)
for t, (p1, p2, _) in graph.items():
    in_edges[t].add(p1)
    in_edges[t].add(p2)

sorted_list = []
no_inc_edges = set()
for p in all_ps:
    edges = in_edges[p]
    if len(edges) == 0:
        no_inc_edges.add(p)

while len(no_inc_edges) > 0:
    node = no_inc_edges.pop()
    sorted_list.append(node)
    for p in in_edges:
        if node in in_edges[p]:
            in_edges[p].remove(node)
            if len(in_edges[p]) == 0:
                no_inc_edges.add(p)

for node in sorted_list:
    if node in vals:
        continue
    p1, p2, rule = graph[node]
    v1 = vals[p1]
    v2 = vals[p2]
    vals[node] = rule(v1, v2)

z_nodes = []
for node in all_ps:
    if node[0] == 'z':
        z_nodes.append(node)

z_nodes = sorted(z_nodes)[::-1]
v = 0
for node in z_nodes:
    v = (v << 1) + vals[node]

print(v)
