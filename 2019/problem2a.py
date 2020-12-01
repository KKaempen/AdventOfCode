nums = input("")
inst = nums.split(",")
for i in range(len(inst)):
    inst[i] = int(inst[i])

inst[1] = 12
inst[2] = 2

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

print("Position 0: " + str(inst[0]))
