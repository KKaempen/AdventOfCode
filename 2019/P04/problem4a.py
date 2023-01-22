data = []
with open("problem4.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

lo, hi = [int(x) for x in data[0].split('-')]

total = 0
for p in range(lo, hi + 1):
    s = str(p)
    has_double = False
    ascends = True
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            ascends = False
            break
        if s[i + 1] == s[i]:
            has_double = True
    if has_double and ascends:
        total += 1

print(total)
