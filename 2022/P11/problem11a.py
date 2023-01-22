data = []
with open("problem11.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = '\n'.join(data).split('\n\n')

def get_monkey_func(op, inp1, inp2):
    if op == '*':
        return lambda x: (x if inp1 == 'old' else int(inp1)) * (x if inp2 == 'old' else int(inp2))
    if o_detail[1] == '+':
        return lambda x: (x if inp1 == 'old' else int(inp1)) + (x if inp2 == 'old' else int(inp2))

monkeys = []
for d in data:
    expanded = d.split('\n')
    start_items_list = expanded[1].replace('Starting items: ', '')
    start_items = [int(x) for x in start_items_list.split(', ')]
    operation = expanded[2].split(' = ')[1]
    o_detail = operation.split()
    test = int(expanded[3].replace('Test: divisible by ', ''))
    true = int(expanded[4].replace('If true: throw to monkey ', ''))
    false = int(expanded[5].replace('If false: throw to monkey ', ''))
    monkeys.append((start_items.copy(), get_monkey_func(o_detail[1], o_detail[0], o_detail[2]), test, true, false))


item_checks = [0 for m in monkeys]
for i in range(20):
    for j in range(len(monkeys)):
        items, func, test, true, false = monkeys[j]
        item_checks[j] += len(items)
        while len(items) > 0:
            item = items.pop(0)
            new_item = func(item)
            new_item = new_item // 3
            if new_item % test == 0:
                monkeys[true][0].append(new_item)
            else:
                monkeys[false][0].append(new_item)

item_checks = sorted(item_checks, reverse=True)
print(item_checks[0] * item_checks[1])
