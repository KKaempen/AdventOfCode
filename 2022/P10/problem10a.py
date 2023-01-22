data = []
with open("problem10.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

important_nums = {20, 60, 100, 140, 180, 220}
tot = 0
reg_val = 1
#to_add = [0, 0]
#for i in range(1, 221):
#    d = data[i - 1] if i - 1 < len(data) else ' '
#    inst = d.split()
#    amount = 0
#    if d[0] == 'addx':
#        amount = int(d[1])
#    if i in important_nums:
#        tot += reg_val * i
#    reg_val += to_add[-1]
#    for j in range(len(to_add) - 1, 0, -1):
#        to_add[j] = to_add[j - 1]
#    to_add[0] = amount
cycle_val = 1
inst_idx = -1
inst_timer = 0
amount = 0
while inst_idx < len(data):
# Start of cycle
    if inst_timer == 0:
        inst_idx += 1
        if inst_idx >= len(data):
            break
        inst = data[inst_idx].split()
        if inst[0] == 'addx':
            amount = int(inst[1])
            inst_timer = 2
        else:
            amount = 0
# During cycle
    if cycle_val in important_nums:
        tot += reg_val * cycle_val
    cycle_val += 1
# After cycle
    if inst_timer > 1:
        inst_timer -= 1
        continue
    if inst_timer == 1:
        reg_val += amount
        inst_timer -= 1

print(tot)
