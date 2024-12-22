from collections import defaultdict

data = []
with open("problem22.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data]

prune_val = 16777216
sequences = defaultdict(int)
for num in data:
    curr_val = num % 10
    last_diffs = tuple(0 for i in range(4))
    seen_tuples = set()
    for i in range(2000):
        r = num * 64
        num = (num ^ r) % prune_val
        r = num // 32
        num = (num ^ r) % prune_val
        r = num * 2048
        num = (num ^ r) % prune_val
        next_val = num % 10
        diff = next_val - curr_val
        last_diffs = last_diffs[1:] + (diff,)
        curr_val = next_val
        if i >= 3 and last_diffs not in seen_tuples:
            sequences[last_diffs] += curr_val
            seen_tuples.add(last_diffs)

print(max(sequences.values()))
