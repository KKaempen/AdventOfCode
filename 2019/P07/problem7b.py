import itertools

data = []
with open("problem7.txt", 'r') as f:
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
    return idx + 4

def intcode_mul(idx, insts, m1, m2):
    p1, p2, dest = get_intcode_params(idx, insts, 3, m1, m2)
    insts[dest] = p1 * p2
    return idx + 4

def intcode_inp(idx, insts, inp):
    s = get_intcode_params(idx, insts, 1)
    insts[s] = inp
    return idx + 2

def intcode_out(idx, insts, m1):
    p = get_intcode_params(idx, insts, 1, m1)
    return idx + 2, p

def intcode_jmp(idx, insts, jump_if, m1, m2):
    p1, p2 = get_intcode_params(idx, insts, 2, m1, m2)
    if (p1 == 0) ^ jump_if:
        return p2
    else:
        return idx + 3

def intcode_lst(idx, insts, m1, m2):
    p1, p2, dest = get_intcode_params(idx, insts, 3, m1, m2)
    to_store = 1 if p1 < p2 else 0
    insts[dest] = to_store
    return idx + 4

def intcode_equ(idx, insts, m1, m2):
    p1, p2, dest = get_intcode_params(idx, insts, 3, m1, m2)
    to_store = 1 if p1 == p2 else 0
    insts[dest] = to_store
    return idx + 4

def run_intcode(data, perm):
    inst_list = [data.copy() for i in range(5)]
    idxs = [0 for i in range(5)]
    perm_idx = 0
    insts = inst_list[perm_idx]
    idx = idxs[perm_idx]
    inps = [perm[perm_idx], 0]
    inp_idx = 0
    max_sig = 0
    op = insts[idx]
    while op != 99:
        m1 = (op // 100) % 10
        m2 = (op // 1000) % 10
        m3 = (op // 10000) % 10
        op %= 100
        if op == 1:
            idx = intcode_add(idx, insts, m1, m2)
        elif op == 2:
            idx = intcode_mul(idx, insts, m1, m2)
        elif op == 3:
            idx = intcode_inp(idx, insts, inps[inp_idx])
            inp_idx += 1
        elif op == 4:
            idx, out = intcode_out(idx, insts, m1)
            idxs[perm_idx % 5] = idx
            perm_idx += 1
            idx = idxs[perm_idx % 5]
            if perm_idx % 5 == 0:
                max_sig = max(max_sig, out)
            insts = inst_list[perm_idx % 5]
            inp_idx = 0
            inps = [perm[perm_idx]] if perm_idx < 5 else []
            inps.append(out)
        elif op == 5:
            idx = intcode_jmp(idx, insts, True, m1, m2)
        elif op == 6:
            idx = intcode_jmp(idx, insts, False, m1, m2)
        elif op == 7:
            idx = intcode_lst(idx, insts, m1, m2)
        elif op == 8:
            idx = intcode_equ(idx, insts, m1, m2)
        else:
            raise Exception("Unknown opcode")
        op = insts[idx]
    return max_sig

perms = itertools.permutations(range(5, 10))

max_out = 0
for perm in perms:
    out = run_intcode(data.copy(), perm)
    max_out = max(max_out, out)

print(max_out)
