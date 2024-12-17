data = []
with open("problem17.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

regs_str, ops_str = '\n'.join(data).split('\n\n')
regs = [int(x[12:]) for x in regs_str.split('\n')]
ops = [int(x) for x in ops_str[9:].split(',')]

inst_ptr = 0
outs = []
while inst_ptr < len(ops):
    inst = ops[inst_ptr]
    operand = ops[inst_ptr + 1]
    combo_op = lambda x: regs[x - 4] if 4 <= x < 7 else x
    if inst == 0:
        operand = combo_op(operand)
        regs[0] = regs[0] >> operand
    elif inst == 1:
        regs[1] = regs[1] ^ operand
    elif inst == 2:
        operand = combo_op(operand)
        regs[1] = operand % 8
    elif inst == 3:
        if regs[0] != 0:
            inst_ptr = operand - 2
    elif inst == 4:
        regs[1] = regs[1] ^ regs[2]
    elif inst == 5:
        operand = combo_op(operand)
        outs.append(operand % 8)
    elif inst == 6:
        operand = combo_op(operand)
        regs[1] = regs[0] >> operand
    elif inst == 7:
        operand = combo_op(operand)
        regs[2] = regs[0] >> operand
    inst_ptr += 2

print(','.join([str(x) for x in outs]))
