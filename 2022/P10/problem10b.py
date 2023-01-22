data = []
with open("problem10.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

important_nums = {40, 80, 120, 160, 200, 240}
reg_val = 1
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
    if abs(reg_val - ((cycle_val - 1) % 40)) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if cycle_val in important_nums:
        print()
    cycle_val += 1
# After cycle
    if inst_timer > 1:
        inst_timer -= 1
        continue
    if inst_timer == 1:
        reg_val += amount
        inst_timer -= 1

