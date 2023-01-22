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

def get_exact_costs(base, prod, cs):
    if base == prod:
        return {prod: 1.0}
    amt, reacs = cs[prod]
    d = {reac: cost for r in reacs for reac, cost in get_exact_costs(base, r[0], cs).items()}
    b_cost = sum([d[r[0]] * r[1] for r in reacs]) / amt
    d[prod] = b_cost
    return d

def verify_amount(fuel, max_ore, cs, t_sort):
    frontier = [(t_sort['FUEL'], 'FUEL')]
    needed_reacs = {'FUEL': fuel}
    while len(frontier) > 0:
        _, r = heappop(frontier)
        req_amount = needed_reacs[r]
        rcp_amount, reacs = cs[r]
        rcp_count = ceil(req_amount / rcp_amount)
        for reac, amt in reacs:
            if reac in cs and reac not in needed_reacs:
                heappush(frontier, (t_sort[reac], reac))
            if reac not in needed_reacs:
                needed_reacs[reac] = 0
            needed_reacs[reac] += amt * rcp_count
    return needed_reacs['ORE'] <= max_ore
    
d = get_exact_costs('ORE', 'FUEL', costs)
fuel_poss = int(1000000000000 / d['FUEL'])
while not verify_amount(fuel_poss, 1000000000000, costs, topo):
    fuel_poss -= 1
print(fuel_poss)
