import itertools

def run_intcode(inst, in1, in2):
    idx = 0
    inp_n = 1
    while True:
        opc = inst[idx]
        if opc == 99:
            break
        m1 = (opc // 100) % 10
        m2 = (opc // 1000) % 10
        m3 = (opc // 10000) % 10
        opc = opc % 100
        s1 = inst[idx + 1]
        s2 = inst[idx + 2]
        dest = inst[idx + 3]
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
            if inp_n == 1:
                inst[s1] = in1
                inp_n = 2
            elif inp_n == 2:
                inst[s1] = in2
            idx += 2
        elif opc == 4:
            return p1
            idx += 2
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
    raise Exception("Nothing returned")

filename = input("")
f = open(filename, 'r')
nums = f.read()
inst = nums.split(",")
for i in range(len(inst)):
    inst[i] = int(inst[i])

perms = itertools.permutations(range(5))

max_out = 0
for perm in perms:
    inp = 0
    for i in range(5):
        new_inst = inst.copy()
        inp = run_intcode(new_inst, int(perm[i]), inp)
    max_out = max(max_out, inp)

print("Max: " + str(max_out))

