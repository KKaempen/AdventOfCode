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
        if beac[1] == y_lev:
            if beac[0] == int_min:
                int_min += 1
            elif beac[0] == int_max:
                int_max -= 1
        return (int_min, int_max)
    return None

impossible_intervals = [get_impossible_interval(sens, sensors[sens], 2000000) for sens in sensors]
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

print(combined_intervals)

print(sum([x[1] - x[0] + 1 for x in combined_intervals]))
