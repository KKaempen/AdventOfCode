from re import match
from math import ceil, inf

data = []
with open("problem19.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

bps = []
re1 = r'Blueprint (\d+): .*'
re2 = r'.* Each ore robot costs (\d+) ore\..*'
re3 = r'.* Each clay robot costs (\d+) ore\..*'
re4 = r'.* Each obsidian robot costs (\d+) ore and (\d+) clay\..*'
re5 = r'.* Each geode robot costs (\d+) ore and (\d+) obsidian\..*'
for d in data:
    bp_id = int(match(re1, d).groups()[0])
    ore_cost = int(match(re2, d).groups()[0])
    cly_cost = int(match(re3, d).groups()[0])
    obs_cost1, obs_cost2 = [int(x) for x in match(re4, d).groups()]
    gde_cost1, gde_cost2 = [int(x) for x in match(re5, d).groups()]
    bps.append((bp_id, (ore_cost,), (cly_cost,), (obs_cost1, obs_cost2), (gde_cost1, gde_cost2)))

def can_build(bp, resources, r):
    if r == 0:
        return resources[0] >= bp[1][0]
    if r == 1:
        return resources[0] >= bp[2][0]
    if r == 2:
        return resources[0] >= bp[3][0] and resources[1] >= bp[3][1]
    if r == 3:
        return resources[0] >= bp[4][0] and resources[2] >= bp[4][1]
    return None

def update_resources(robs, ress):
    robots = list(robs)
    resources = list(ress)
    for i in range(4):
        resources[i] += robots[i]
    return tuple(robots), tuple(resources)

def build_robot(bp, robs, ress, r):
    if not can_build(bp, ress, r):
        return robs, ress
    robots = list(robs)
    resources = list(ress)
    robots[r] += 1
    if r == 0:
        ore = bp[r + 1][0]
        resources[0] -= ore
    if r == 1:
        ore = bp[r + 1][0]
        resources[0] -= ore
    if r == 2:
        ore, cly = bp[r + 1]
        resources[0] -= ore
        resources[1] -= cly
    if r == 3:
        ore, obs = bp[r + 1]
        resources[0] -= ore
        resources[2] -= obs
    return tuple(robots), tuple(resources)

def time_to_build(bp, robots, resources, r):
    if r == 0:
        ore = bp[r + 1][0]
        ore -= resources[0]
        if robots[0] == 0:
            return inf
        if ore <= 0:
            return 0
        ore_t = ceil(ore / robots[0])
        return ore_t
    if r == 1:
        ore = bp[r + 1][0]
        ore -= resources[0]
        if robots[0] == 0:
            return inf
        if ore <= 0:
            return 0
        ore_t = ceil(ore / robots[0])
        return ore_t
    if r == 2:
        ore, cly = bp[r + 1]
        ore -= resources[0]
        cly -= resources[1]
        if robots[0] == 0 or robots[1] == 0:
            return inf
        if ore <= 0 and cly <= 0:
            return 0
        ore_t = ceil(ore / robots[0])
        cly_t = ceil(cly / robots[1])
        return max(ore_t, cly_t)
    if r == 3:
        ore, obs = bp[r + 1]
        ore -= resources[0]
        obs -= resources[2]
        if robots[0] == 0 or robots[2] == 0:
            return inf
        if ore <= 0 and obs <= 0:
            return 0
        ore_t = ceil(ore / robots[0])
        obs_t = ceil(obs / robots[2])
        return max(ore_t, obs_t)
    return None

def get_quality(bp, t):
    robots = (1, 0, 0, 0)
    resources = (0, 0, 0, 0)
    ore_ore = bp[1][0]
    cly_ore = bp[2][0]
    obs_ore = bp[3][0]
    obs_cly = bp[3][1]
    gde_ore = bp[4][0]
    gde_obs = bp[4][1]
    max_ore = max(ore_ore, cly_ore, obs_ore, gde_ore)
    max_cly = max(obs_cly, 0)
    max_obs = max(gde_obs, 0)
    maxes = [max_ore, max_cly, max_obs]
    state = (robots, resources, t)
    seen = set({})
    frontier = [state]
    best_geodes = 0
    while len(frontier) > 0:
        state = frontier.pop(0)
        if state in seen:
            continue
        seen.add(state)
#        print("New state:", state)
        robots, resources, t_left = state
        if t_left == 0:
            best_geodes = max(best_geodes, resources[3])
        else:
            possible_geodes = (resources[3] + 
                              t_left * robots[3] +
                              (t_left * (t_left - 1)) // 2)
            if possible_geodes <= best_geodes:
                continue
        new_robots, new_resources = (robots, resources)
        if robots[3] > 0:
            for i in range(t_left):
                new_robots, new_resources = update_resources(new_robots, new_resources)
            frontier.append((new_robots, new_resources, 0))
        for i in range(3, -1, -1):
            if i < len(maxes) and robots[i] >= maxes[i]:
                continue
            new_robots, new_resources = robots, resources
            ttb = time_to_build(bp, robots, resources, i)
            if ttb < t_left:
#                print("Time to build", i, "is", ttb)
#                print()
                for j in range(ttb + 1):
                    new_robots, new_resources = update_resources(new_robots, new_resources)
                new_robots, new_resources = build_robot(bp, new_robots, new_resources, i)
                frontier.append((new_robots, new_resources, t_left - (ttb + 1)))
    return best_geodes

total = 1
for bp in bps[:3]:
#    print("Processing blueprint", bp[0])
#    print(bp[1:])
#    print()
    total *= get_quality(bp, 32)
print(total)

