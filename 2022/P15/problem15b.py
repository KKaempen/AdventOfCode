data = []
with open("problem15.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [x.replace('Sensor at x=', '').replace('closest beacon is at x=', '').replace(' y=', '') for x in data]
data = [x.split(': ') for x in data]
data = [[[int(y) for y in z.split(',')] for z in x] for x in data]

sensors = {tuple(x[0]) : tuple(x[1]) for x in data}

def get_impossible_interval(sens, beac, y_lev):
    man_dist = abs(sens[0] - beac[0]) + abs(sens[1] - beac[1])
    available_dist = man_dist - abs(y_lev - sens[1])
    if available_dist >= 0:
        int_min = sens[0] - available_dist
        int_max = sens[0] + available_dist
        return (int_min, int_max)
    return None

def get_comp_intvs(intvs, m, M):
    comp_intvs = []
    if intvs[0][0] > m:
        comp_intvs.append((m, intvs[0][0] - 1))
    for i in range(len(intvs) - 1):
        lo = intvs[i][1] + 1
        hi = intvs[i + 1][0] - 1
        if lo <= hi and lo >= m and hi <= M:
            comp_intvs.append((lo, hi))
    if intvs[-1][1] < M:
        comp_intvs.append((intvs[-1][1] + 1, M))
    return comp_intvs

for y in range(4000001):
    impossible_intervals = [get_impossible_interval(sens, sensors[sens], y) for sens in sensors]
    impossible_intervals = [x for x in impossible_intervals if x]
    impossible_intervals = sorted(impossible_intervals)

    combined_intervals = [impossible_intervals[0]]
    for intv in impossible_intervals[1:]:
        curr_int = combined_intervals.pop()
        if intv[0] <= curr_int[1]:
            high_val = max(curr_int[1], intv[1])
            new_int = (curr_int[0], high_val)
            combined_intervals.append(new_int)
        else:
            combined_intervals.append(curr_int)
            combined_intervals.append(intv)

    comp_intvs = get_comp_intvs(combined_intervals, 0, 4000000)
    if len(comp_intvs) > 0:
        x = comp_intvs[0][0]
        print(x * 4000000 + y)
