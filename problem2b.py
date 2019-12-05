def getResult(inst):
    idx = 0
    while True:
        if inst[idx] == 99:
            break
        s1 = inst[idx + 1]
        s2 = inst[idx + 2]
        dest = inst[idx + 3]
        if inst[idx] == 1:
            inst[dest] = inst[s1] + inst[s2]
        elif inst[idx] == 2:
            inst[dest] = inst[s1] * inst[s2]
        else:
            raise Exception("Unknown opcode")
        idx += 4
    return inst[0]

nums = input("")
inst_orig = nums.split(",")
for i in range(len(inst_orig)):
    inst_orig[i] = int(inst_orig[i])

for n in range(100):
    for v in range(100):
        inst = inst_orig.copy()
        inst[1] = n
        inst[2] = v
        if getResult(inst) == 19690720:
            print("Answer: " + str(100 * n + v))



