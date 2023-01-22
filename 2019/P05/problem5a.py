data = []
with open("problem5.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data[0].split(',')]

def get_intcode_params(idx, insts, num, m1=1, m2=1, m3=1):
    params = []
    ms = [m1, m2, m3]
    for i in range(1, num + 1):
        p = insts[idx + i]
        p = insts[p] if ms[i - 1] == 0 else p
        params.append(p)
    return params if len(params) > 1 else params[0]

def intcode_add(idx, insts, m1, m2):
    p1, p2, dest = get_intcode_params(idx, insts, 3, m1, m2)
    insts[dest] = p1 + p2
    return 4

def intcode_mul(idx, insts, m1, m2):
    p1, p2, dest = get_intcode_params(idx, insts, 3, m1, m2)
    insts[dest] = p1 * p2
    return 4

def intcode_inp(idx, insts, inp):
    s = get_intcode_params(idx, insts, 1)
    insts[s] = inp
    return 2

def intcode_out(idx, insts, m1):
    p = get_intcode_params(idx, insts, 1, m1)
    print(p)
    return 2

idx = 0
op = data[idx]
inps = [1]
inp_idx = 0
while op != 99:
    m1 = (op // 100) % 10
    m2 = (op // 1000) % 10
    m3 = (op // 10000) % 10
    op %= 100
    if op == 1:
        idx += intcode_add(idx, data, m1, m2)
    elif op == 2:
        idx += intcode_mul(idx, data, m1, m2)
    elif op == 3:
        idx += intcode_inp(idx, data, inps[inp_idx])
        inp_idx += 1
    elif op == 4:
        idx += intcode_out(idx, data, m1)
    else:
        raise Exception("Unknown opcode")
    op = data[idx]
