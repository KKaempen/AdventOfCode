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

def calculate_monkey_tree(m, d):
    val = d[m]
    if val[0] in ops:
        f = ops[val[0]]
        t1 = calculate_monkey_tree(val[1], d)
        t2 = calculate_monkey_tree(val[2], d)
        return f(t1, t2)
    else:
        return val[0]
    
print(calculate_monkey_tree('root', new_data))
