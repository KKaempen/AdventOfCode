data = []
with open("problem21.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [x.split(': ') for x in data]

ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}

new_data = {}
for d in data:
    d1 = d[0]
    d2 = d[1]
    for c in ops:
        if c in d2:
            p1, p2 = d2.split(' ' + c + ' ')
            new_data[d1] = (c, p1, p2)
            break
    else:
        new_data[d1] = (int(d2),)

def find_humn_branch(d, m):
    if m == 'humn':
        return []
    t = d[m]
    if len(t) == 1:
        return None
    _, m1, m2 = t
    a1 = find_humn_branch(d, m1)
    a2 = find_humn_branch(d, m2)
    if a1 != None and a2 != None:
        raise Exception("ERROR: FOUND HUMN IN NON-HUMN BRANCH")
    if a1 == None and a2 == None:
        return None
    if a1 != None:
        return [m1] + a1
    elif a2 != None:
        return [m2] + a2

def calculate_monkey_tree(m, d):
    if m == 'humn':
        raise Exception("ERROR: FOUND HUMN IN NON-HUMN BRANCH")
    val = d[m]
    if val[0] in ops:
        f = ops[val[0]]
        t1 = calculate_monkey_tree(val[1], d)
        t2 = calculate_monkey_tree(val[2], d)
        return f(t1, t2)
    else:
        return val[0]

def reverse_engineer_val(v, m, humn_idx, humn, d):
    if m == 'humn':
        return v
    op, m1, m2 = d[m]
    h_b, non_h = (m1, m2) if humn[humn_idx] == m1 else (m2, m1)
    val = calculate_monkey_tree(non_h, d)
    if op == '+':
        return reverse_engineer_val(v - val, h_b, humn_idx + 1, humn, d)
    elif op == '-':
        if non_h == m1:
            return reverse_engineer_val(val - v, h_b, humn_idx + 1, humn, d)
        elif non_h == m2:
            return reverse_engineer_val(v + val, h_b, humn_idx + 1, humn, d)
    elif op == '*':
        return reverse_engineer_val(v // val, h_b, humn_idx + 1, humn, d) 
    elif op == '/':
        if non_h == m1:
            return reverse_engineer_val(val // v, h_b, humn_idx + 1, humn, d)
        elif non_h == m2:
            return reverse_engineer_val(v * val, h_b, humn_idx + 1, humn, d)

humn = find_humn_branch(new_data, 'root')
_, m1, m2 = new_data['root'] 
non_h, h_b = (m1, m2) if m2 == humn[0] else (m2, m1)
target_val = calculate_monkey_tree(non_h, new_data)
print(reverse_engineer_val(target_val, h_b, 1, humn, new_data))
