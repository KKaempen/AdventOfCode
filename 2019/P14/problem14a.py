from math import ceil
from heapq import heappush, heappop

data = []
with open("problem14.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

costs = {}
for d in data:
    reacs, prod = d.split(' => ')
    prod_num, prod_name = prod.split(' ')
    prod_num = int(prod_num)
    reac_list = []
    for r in reacs.split(', '):
        reac_num, reac_name = r.split(' ')
        reac_num = int(reac_num)
        reac_list.append((reac_name, reac_num))
    costs[prod_name] = (prod_num, reac_list)

topo = {'FUEL': 0}
frontier = [(0, 'FUEL')]
while len(frontier) > 0:
    order, r = heappop(frontier)
    if r not in topo:
        topo[r] = order
    order = max(topo[r], order)
    topo[r] = order
    if r not in costs:
        continue
    for reac, _ in costs[r][1]:
        heappush(frontier, (order + 1, reac))

frontier = [(topo['FUEL'], 'FUEL')]
needed_reacs = {'FUEL': 1}
while len(frontier) > 0:
    _, r = heappop(frontier)
    req_amount = needed_reacs[r]
    rcp_amount, reacs = costs[r]
    rcp_count = ceil(req_amount / rcp_amount)
    for reac, amt in reacs:
        if reac in costs and reac not in needed_reacs:
            heappush(frontier, (topo[reac], reac))
        if reac not in needed_reacs:
            needed_reacs[reac] = 0
        needed_reacs[reac] += amt * rcp_count

print(needed_reacs['ORE'])
