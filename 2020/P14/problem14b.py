data = open('problem14.txt', 'r').read().splitlines()

def make_addrs(mask):
    masks = []
    mask = [x for x in mask]
    bits = mask.count('X')
    for num in range(int(2**bits)):
        s = ''
        for i in range(bits):
            s = str(num % 2) + s
            num = num // 2
        cur_mask = list(mask)
        try:
            idx = cur_mask.index('X')
        except:
            idx = -1
        counter = 0
        while idx != -1:
            cur_mask[idx] = s[counter]
            counter += 1
            try:
                idx = cur_mask.index('X')
            except:
                idx = -1
        masks.append(''.join(cur_mask))
    return masks

mems = {}
mask = ''
for inst in data:
    b = inst.split(' = ')
    if b[0] == 'mask':
        mask = b[1]
    else:
        addr = int(b[0].split('[')[1][:-1])
        addr_l = []
        for i in range(36):
            addr_l = [str(addr % 2)] + addr_l
            addr = addr // 2
        for i in range(36):
            if mask[i] == 'X':
                addr_l[i] = 'X'
            else:
                addr_l[i] = str(int(addr_l[i]) | int(mask[i]))
        addrs = make_addrs(addr_l)
        val = int(b[1])
        for a in addrs:
            mems[int(a, 2)] = val

print(sum([mems[x] for x in mems]))
