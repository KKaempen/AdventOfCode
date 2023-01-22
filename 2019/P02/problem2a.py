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

data[1] = 12
data[2] = 2

idx = 0
op = data[idx]
while op != 99:    
    if op == 1:
        idx += intcode_add(idx, data)
    elif op == 2:
        idx += intcode_mul(idx, data)
    else:
        raise Exception("Unknown opcode")
    op = data[idx]

print(data[0])
