data = open('problem14.txt', 'r').read().splitlines()

mems = [0 for i in range(int(2**16))]
maskA = int('1' * 36, 2)
maskO = int('0' * 36, 2)
for inst in data:
    b = inst.split(' = ')
    if b[0] == 'mask':
        maskA = int(''.join(['1' if x == 'X' else '0' for x in b[1]]), 2)
        maskO = int(''.join(['0' if x == 'X' else x for x in b[1]]), 2)
    else:
        addr = int(b[0].split('[')[1][:-1])
        val = int(b[1])
        mems[addr] = (val & maskA) | maskO

print(sum(mems))
