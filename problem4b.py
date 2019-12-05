num_range = input("")
lo, hi = num_range.split("-")
lo = int(lo)
hi = int(hi)

total = 0
for p in range(lo, hi + 1):
    p_str = str(p)
    works = False
    i = 0
    while i < len(p_str) - 1:
        c = p_str[i]
        c_n = p_str[i + 1]
        if c == c_n:
            idx = i + 2
            while idx < len(p_str) and p_str[idx] == c:
                idx += 1
            if idx == i + 2:
                works = True
            i = idx - 1
            continue
        elif c > c_n:
            works = False
            break
        i += 1
    if works:
        total += 1

print("Total: " + str(total))
