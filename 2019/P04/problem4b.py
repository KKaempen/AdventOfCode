data = []
with open("problem4.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

lo, hi = [int(x) for x in data[0].split('-')]

total = 0
for p in range(lo, hi + 1):
    s = str(p)
    has_double = False
    ascends = True
    i = 0
    while i < len(s) - 1:
        if s[i + 1] < s[i]:
            ascends = False
            break
        if s[i + 1] == s[i]:
            j = 2
            while i + j < len(s) and s[i] == s[i + j]:
                j += 1
            if j == 2:
                has_double = True
            i += j - 2
        i += 1
    if has_double and ascends:
        total += 1

print(total)
