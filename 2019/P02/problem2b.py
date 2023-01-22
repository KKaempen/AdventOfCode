data = []
with open("problem2.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data[0].split(',')]

def intcode_add(idx, insts):
    s1 = insts[idx + 1]
    s2 = insts[idx + 2]
    dest = insts[idx + 3]
    insts[dest] = insts[s1] + insts[s2]
    return 4

def intcode_mul(idx, insts):
    s1 = insts[idx + 1]
    s2 = insts[idx + 2]
    dest = insts[idx + 3]
    insts[dest] = insts[s1] * insts[s2]
    return 4

def process_intcode(insts, arg1, arg2):
    insts[1] = arg1
    insts[2] = arg2

    idx = 0
    op = insts[idx]
    while op != 99:    
        if op == 1:
            idx += intcode_add(idx, insts)
        elif op == 2:
            idx += intcode_mul(idx, insts)
        else:
            raise Exception("Unknown opcode")
        op = insts[idx]
    return insts[0]

for n in range(100):
    for v in range(100):
        if process_intcode(data.copy(), n, v) == 19690720:
            print(100 * n + v)
            break
