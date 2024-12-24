from collections import defaultdict, deque
from random import randrange

data = []
with open("problem24.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

swaps = [('dhg', 'z06'), ('brk', 'dpd'), ('bhd', 'z23'), ('nbf', 'z38')]

inits, rules = '\n'.join(data).split('\n\n')
graph = {}
all_ps = set()
for rule in rules.split('\n'):
    preds, term = rule.split(' -> ')
    p1, p2, rule = (None, None, None)
    if 'XOR' in preds:
        p1, p2 = preds.split(' XOR ')
        rule = '^'
    elif 'OR' in preds:
        p1, p2 = preds.split(' OR ')
        rule = '|'
    elif 'AND' in preds:
        p1, p2 = preds.split(' AND ')
        rule = '&'
    all_ps.add(term)
    all_ps.add(p1)
    all_ps.add(p2)
    graph[term] = (p1, p2, rule)

for s1, s2 in swaps:
    g1 = graph[s1]
    graph[s1] = graph[s2]
    graph[s2] = g1

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

def get_carry_str(level):
    if level == 0:
        return "(y00) & (x00)"
    next_carry = get_carry_str(level - 1)
    suffix = "0" + str(level) if level < 10 else str(level)
    return f"((y{suffix}) & (x{suffix})) | (((y{suffix}) ^ (x{suffix})) & ({next_carry}))"

z_nodes = sorted([node for node in sorted_list if node[0] == 'z'])
str_reps = {}
for node in sorted_list:
    if node[0] == 'x' or node[0] == 'y':
        str_reps[node] = node
for node in sorted_list:
    if node in str_reps:
        continue
    p1, p2, rule = graph[node]
    first = max(str_reps[p1], str_reps[p2])
    second = min(str_reps[p1], str_reps[p2])
    rep = f"({first}) {rule} ({second})"
    str_reps[node] = rep
for i, node in enumerate(z_nodes):
    if i == 0:
        exp_str = "(y00) ^ (x00)"
    elif i == len(z_nodes) - 1:
        exp_str = get_carry_str(i - 1)
    else:
        carry_str = get_carry_str(i - 1)
        level_str = "0" + str(i) if i < 10 else str(i)
        exp_str = f"((y{level_str}) ^ (x{level_str})) ^ ({carry_str})"
    if exp_str != str_reps[node]:
        print(f"{node}")
        print("----------------------------")
        print(f"Got: {str_reps[node]}")
        print(f"Exp: {exp_str}")
        break
else:
    print(','.join(sorted([x for t in swaps for x in t])))
