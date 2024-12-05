from functools import cmp_to_key
from collections import defaultdict

data = []
with open("problem5.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = ('.'.join(data)).split('..')
rules = data[0]
tests = data[1]

rule_dict = defaultdict(set)
for rule in rules.split('.'):
    p1, p2 = rule.split('|')
    rule_dict[p1].add(p2)

count = 0
for test in tests.split('.'):
    pages = test.split(',')
    works = True
    for p1, p2 in zip(pages[:-1], pages[1:]):
        if p2 not in rule_dict[p1]:
            works = False
            break
    if not works:
        comparator = lambda x, y: -1 if y in rule_dict[x] else 1 if x in rule_dict[y] else 0
        true_list = sorted(pages, key=cmp_to_key(comparator))
        count += int(true_list[len(true_list) // 2])
#        all_pages = set(pages)
#        in_edges = {}
#        for p in all_pages:
#            in_edges[p] = set()
#        for p in all_pages:
#            for out_edge in rule_dict[p] & all_pages:
#                in_edges[out_edge].add(p)
#        sorted_list = []
#        no_inc_edges = set({})
#        for p, edges in in_edges.items():
#            if len(edges) == 0:
#                no_inc_edges.add(p)
#        while len(no_inc_edges) > 0:
#            node = no_inc_edges.pop()
#            sorted_list.append(node)
#            for p in in_edges:
#                if node in in_edges[p]:
#                    in_edges[p].remove(node)
#                    if len(in_edges[p]) == 0:
#                        no_inc_edges.add(p)
#        count += int(sorted_list[len(sorted_list) // 2])

print(count)
