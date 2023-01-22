data = open('problem18.txt', 'r').read().splitlines()

def evaluate(line):
    while '(' in line:
        idx1 = line.find('(') + 1
        idx2 = 0
        paren_val = 1
        for i in range(idx1, len(line)):
            if line[i] == '(':
                paren_val += 1
            elif line[i] == ')':
                if paren_val == 1:
                    idx2 = i
                    break
                else:
                    paren_val -= 1
        r = evaluate(line[idx1:idx2])
        line = line[:idx1 - 1] + str(r) + line[idx2 + 1:]
    prods = line.split(' * ')
    prods = [sum([int(y) for y in x.split(' + ')]) for x in prods]
    total = 1
    for p in prods:
        total *= p
    return total

total = 0
for line in data:
    total += evaluate(line)

print(total)
