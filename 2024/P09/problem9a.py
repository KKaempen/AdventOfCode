data = []
with open("problem9.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

line = [int(c) for c in data[0]]
arr = []

lo = 0
hi = len(line) - 1

lo_id = 0
hi_id = (len(line) - 1) // 2

curr = 0
while lo < hi:
    if curr == 0:
        curr = line[lo]
        print(f"Setting curr to {curr} at idx {lo}")
    if lo % 2 == 0:
        print(f"Filling up from front at idx {lo}")
        for i in range(curr):
            arr.append(lo_id)
        lo += 1
        lo_id += 1
        curr = 0
    else:
        for i in range(min(line[hi], curr)):
            print(f"Filling up from back at idx {hi}")
            arr.append(hi_id)
            line[hi] -= 1
            curr -= 1
        if line[hi] == 0:
            hi -= 2
            hi_id -= 1
        if curr == 0:
            lo += 1
for i in range(line[hi]):
    arr.append(hi_id)

print(arr)
total = sum(i * x for i, x in enumerate(arr))
print(total)


