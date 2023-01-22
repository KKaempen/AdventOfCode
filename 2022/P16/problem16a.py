data = []
with open("problem16.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [x.replace('Valve ', '').replace('tunnels lead to valves ', '').replace('tunnel leads to valve ', '').split('; ') for x in data]
valves = {}
for d in data:
    p1 = d[0]
    p2 = d[1]
    valve_inf = p1.split(' has flow rate=')
    v_name = valve_inf[0]
    v_flow = int(valve_inf[1])
    tunnels = p2.split(', ')
    valves[v_name] = (v_flow, tunnels)

important_valves = {v: valves[v] for v in valves if valves[v][0] > 0}
def get_shortest_paths(vs, v):
    shortest_paths = {}
    frontier = [(v, 0)]
    while len(frontier) > 0:
        curr_v, d = frontier.pop(0)
        if curr_v in shortest_paths:
            continue
        shortest_paths[curr_v] = d
        for next_v in valves[curr_v][1]:
            frontier.append((next_v, d + 1))
    return {v: shortest_paths[v] for v in shortest_paths if v in vs}

valve_map = {v: get_shortest_paths(important_valves, v) for v in important_valves}
valve_map['AA'] = get_shortest_paths(important_valves, 'AA')
open_valves = {v: False for v in important_valves}

def simulate_order(v_map, perm):
    flow_rate = 0
    curr = 'AA'
    total = 0
    t_r = 30
    for next_v in perm:
        time = v_map[curr][next_v] + 1
        curr = next_v
        time = min(time, t_r)
        total += flow_rate * time
        t_r -= time
        flow_rate += valves[curr][0]
    total += flow_rate * t_r
    return total

def get_possible_paths(v_map, start, used, time):
    paths = []
    used.add(start)
    for v in v_map[start]:
        if v in used:
            continue
        to_go = v_map[start][v] + 1
        if to_go < time:
            new_paths = get_possible_paths(v_map, v, used.copy(), time - to_go)
            paths += [[v] + p for p in new_paths]
    paths.append([])
    return paths

possible_paths = get_possible_paths(valve_map, 'AA', set({}), 30)
M = 0
for p in possible_paths:
    s = simulate_order(valve_map, p)
    M = max(s, M)

print(M)
