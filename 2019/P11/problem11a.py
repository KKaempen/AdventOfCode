data = []
with open("problem11.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data[0].split(',')]

def adjust_inst_size(insts, needed_idx):
    curr_size = len(insts)
    add_size = needed_idx - curr_size + 1
    if add_size > 0:
        insts += [0 for i in range(add_size)]
#        print("curr_size:", curr_size)
#        print("add_size:", add_size)
#        print("New length:", len(insts))
#        print()

def get_intcode_params(idx, insts, rel_base, num, m1=1, m2=1, m3=1, dest_param=-1):
    params = []
    ms = [m1, m2, m3]
    for i in range(1, num + 1):
        p = insts[idx + i]
        if ms[i - 1] == 2:
            if dest_param == i:
                p = p + rel_base
            else:
                adjust_inst_size(insts, p + rel_base)
                p = insts[p + rel_base]
        elif ms[i- 1] == 1:
            p = p
        elif ms[i - 1] == 0:
            if dest_param == i:
                p = p
            else:
                adjust_inst_size(insts, p)
                p = insts[p]
        params.append(p)
    return params if len(params) > 1 else params[0]

def intcode_add(idx, insts, rel_base, m1, m2, m3):
#    print("Add")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    p1, p2, dest = get_intcode_params(idx, insts, rel_base, 3, m1, m2, m3, dest_param=3)
#    print(p1, "+", p2, "->", dest)
#    print()
    adjust_inst_size(insts, dest)
    insts[dest] = p1 + p2
    return idx + 4

def intcode_mul(idx, insts, rel_base, m1, m2, m3):
#    print("Mul")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    p1, p2, dest = get_intcode_params(idx, insts, rel_base, 3, m1, m2, m3, dest_param=3)
#    print(p1, "*", p2, "->", dest)
#    print()
    adjust_inst_size(insts, dest)
    insts[dest] = p1 * p2
    return idx + 4

def intcode_inp(idx, insts, rel_base, inp, m1):
#    print("Inp")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    s = get_intcode_params(idx, insts, rel_base, 1, m1, dest_param=1)
#    print(inp, "->", s)
#    print()
    adjust_inst_size(insts, s)
    insts[s] = inp
    return idx + 2

def intcode_out(idx, insts, rel_base, m1):
#    print("Out")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    p = get_intcode_params(idx, insts, rel_base, 1, m1)
#    print(p)
#    print()
    return idx + 2, p

def intcode_jmp(idx, insts, rel_base, jump_if, m1, m2):
#    print("Jmp")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    p1, p2 = get_intcode_params(idx, insts, rel_base, 2, m1, m2)
#    print("If", p1, "== 0 is", jump_if, "jump to", p2)
#    print()
    if (p1 == 0) ^ jump_if:
        return p2
    else:
        return idx + 3

def intcode_lst(idx, insts, rel_base, m1, m2, m3):
#    print("Lst")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    p1, p2, dest = get_intcode_params(idx, insts, rel_base, 3, m1, m2, m3, dest_param=3)
#    print("If", p1, "<", p2, "store to", dest)
#    print()
    adjust_inst_size(insts, dest)
    to_store = 1 if p1 < p2 else 0
    insts[dest] = to_store
    return idx + 4

def intcode_equ(idx, insts, rel_base, m1, m2, m3):
#    print("Equ")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    p1, p2, dest = get_intcode_params(idx, insts, rel_base, 3, m1, m2, m3, dest_param=3)
#    print("If", p1, "==", p2, "store to", dest)
#    print()
    adjust_inst_size(insts, dest)
    to_store = 1 if p1 == p2 else 0
    insts[dest] = to_store
    return idx + 4

def intcode_rel(idx, insts, rel_base, m1):
#    print("Rel")
#    print("Idx:", idx)
#    print("insts[", idx, ":", idx + 4, "]")
#    print(insts[idx: idx + 4])
#    print("rel_base:", rel_base)
    p = get_intcode_params(idx, insts, rel_base, 1, m1)
#    print("Increase rel_base by", p)
#    print()
    rel_base += p
    return idx + 2, rel_base

def run_intcode(data):
    rob_pos = (0, 0)
    rob_dir = (0, 1)
    to_move = 0
    colors = {}

    insts = data.copy()
    idx = 0
    inps = [0]
    inp_idx = 0
    rel_base = 0
    op = insts[idx]
    while op != 99:
        m1 = (op // 100) % 10
        m2 = (op // 1000) % 10
        m3 = (op // 10000) % 10
        op %= 100
        if op == 1:
            idx = intcode_add(idx, insts, rel_base, m1, m2, m3)
        elif op == 2:
            idx = intcode_mul(idx, insts, rel_base, m1, m2, m3)
        elif op == 3:
            inp = colors[rob_pos] if rob_pos in colors else 0
            idx = intcode_inp(idx, insts, rel_base, inp, m1)
        elif op == 4:
            idx, out = intcode_out(idx, insts, rel_base, m1)
            if to_move == 1:
                x, y = rob_dir
                if out == 0:
                    rob_dir = (-y, x)
                elif out == 1:
                    rob_dir = (y, -x)
                rob_pos = (rob_pos[0] + rob_dir[0], rob_pos[1] + rob_dir[1])
            elif to_move == 0:
                colors[rob_pos] = out
            to_move = 1 - to_move
        elif op == 5:
            idx = intcode_jmp(idx, insts, rel_base, True, m1, m2)
        elif op == 6:
            idx = intcode_jmp(idx, insts, rel_base, False, m1, m2)
        elif op == 7:
            idx = intcode_lst(idx, insts, rel_base, m1, m2, m3)
        elif op == 8:
            idx = intcode_equ(idx, insts, rel_base, m1, m2, m3)
        elif op == 9:
            idx, rel_base = intcode_rel(idx, insts, rel_base, m1)
        else:
            raise Exception("Unknown opcode")
        op = insts[idx]
    print(len(colors))

run_intcode(data)
