import itertools
from math import isnan

def run_intcode(inst, s, in1, in2):
    idx = s
    inp_n = 1
    while idx < len(inst):
        opc = inst[idx]
        if opc == 99:
            break
        m1 = (opc // 100) % 10
        m2 = (opc // 1000) % 10
        m3 = (opc // 10000) % 10
        opc = opc % 100
        s1 = float('nan') if idx + 1 >= len(inst) else inst[idx + 1]
        s2 = float('nan') if idx + 2 >= len(inst) else inst[idx + 2]
        dest = float('nan') if idx + 3 >= len(inst) else inst[idx + 3]
        p1 = s1
        p2 = s2
        try:
            if m1 == 0:
                p1 = inst[s1]
            if m2 == 0:
                p2 = inst[s2]
        except:
            pass
        if opc == 1:
            inst[dest] = p1 + p2
            idx += 4
        elif opc == 2:
            inst[dest] = p1 * p2
            idx += 4
        elif opc == 3:
            if inp_n == 1 and not isnan(in1):
                inst[s1] = in1
                inp_n += 1
            else:
                inst[s1] = in2
            idx += 2
        elif opc == 4:
            idx += 2
            return idx, p1
        elif opc == 5:
            if p1 != 0:
                idx = p2
            else:
                idx += 3
        elif opc == 6:
            if p1 == 0:
                idx = p2
            else:
                idx += 3
        elif opc == 7:
            if p1 < p2:
                inst[dest] = 1
            else:
                inst[dest] = 0
            idx += 4
        elif opc == 8:
            if p1 == p2:
                inst[dest] = 1
            else:
                inst[dest] = 0
            idx += 4
        else:
            raise Exception("Unknown opcode")
    if idx >= len(inst):
        print(inst)
        raise Exception("Out of bounds")
    return idx, float('nan')

filename = input("")
f = open(filename, 'r')
nums = f.read()
inst = nums.split(",")
for i in range(len(inst)):
    inst[i] = int(inst[i])

perms = itertools.permutations(range(5, 10))

max_out = 0
for perm in perms:
    inp = 0
    last_good_inp = 0
    new_insts = [inst.copy() for i in range(5)]
    starts = [0 for i in range(5)]
    done_before = False
    while True:
        was_nan = False
        for i in range(5):
            code = float('nan') if done_before else int(perm[i])
            new_start, inp = run_intcode(new_insts[i], starts[i], code, inp)
            starts[i] = new_start
            if new_insts[i] == inst:
                raise Exception("Instructions unchanged")
            if isnan(inp):
                was_nan = True
                break
        done_before = True
        if was_nan:
            max_out = max(max_out, last_good_inp)
            break
        else:
            last_good_inp = inp

print("Max: " + str(max_out))

