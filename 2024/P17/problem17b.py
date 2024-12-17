from collections import deque

data = []
with open("problem17.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

ops_str = data[-1]
ops = [int(x) for x in ops_str[9:].split(',')]

potential_as = deque()
potential_as.append(0)
for op in ops[::-1]:
    num_as = len(potential_as)
    for _ in range(num_as):
        a = potential_as.popleft()
        for last_three in range(8):
            new_a = (a << 3) + last_three
            shift = last_three ^ 7
            c = (new_a >> shift) % 8
            if c ^ last_three == op:
                potential_as.append(new_a)

print(min(potential_as))
