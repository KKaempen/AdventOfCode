num_range = input("")
lo, hi = num_range.split("-")
lo = int(lo)
hi = int(hi)

total = 0
for p in range(lo, hi + 1):
    p_str = str(p)
    works = False
    for i in range(len(p_str) - 1):
        c = p_str[i]
        c_n = p_str[i + 1]
        if c == c_n:
            works = True
        elif c > c_n:
            works = False
            break
    if works:
        total += 1

print("Total: " + str(total))
