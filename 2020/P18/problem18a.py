data = open('problem18.txt', 'r').read().splitlines()

def evaluate(line):
    total = 0
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
    last_op = '+'
    num_start = 0
    i = 0
    while i < len(line):
        if not line[i].isdigit():
            num = int(line[num_start:i])
            if last_op == '+':
                total += num
            elif last_op == '*':
                total *= num
            last_op = line[i + 1]
            num_start = i + 3
            i += 4
        else:
            i += 1
    num = int(line[num_start:])
    if last_op == '+':
        total += num
    elif last_op == '*':
        total *= num
    return total

total = 0
for line in data:
    total += evaluate(line)

print(total)
