data = open('problem16.txt', 'r').read().splitlines()

break1 = data.index('')
break2 = data.index('', break1 + 1)
rules = data[:break1]
my_ticket = [int(x) for x in data[break1 + 2].split(',')]
other_tickets = data[break2 + 2:]
ticket_size = len(my_ticket)

rules_d = {}
for rule in rules:
    rule_name = rule.split(': ')[0]
    rule_desc = rule.split(': ')[1]
    rule_r1 = rule_desc.split(' or ')[0]
    rule_r2 = rule_desc.split(' or ')[1]
    rule_r1 = (int(rule_r1.split('-')[0]), int(rule_r1.split('-')[1]))
    rule_r2 = (int(rule_r2.split('-')[0]), int(rule_r2.split('-')[1]))
    lo1 = rule_r1[0]
    hi1 = rule_r1[1]
    lo2 = rule_r2[0]
    hi2 = rule_r2[1]
    rules_d[rule_name] = (lo1, hi1, lo2, hi2)

bad_idx = set({})
for i, ticket in enumerate(other_tickets):
    vals = [int(x) for x in ticket.split(',')]
    for val in vals:
        for rule in rules_d:
            bounds = rules_d[rule]
            if bounds[0] <= val <= bounds[1] or bounds[2] <= val <= bounds[3]:
                break
        else:
            bad_idx.add(i)

rule_idxs = {}
idxs = set(range(ticket_size))
for rule in rules_d:
    bounds = rules_d[rule]
    possible_idxs = list(range(ticket_size))
    for idx in idxs:
        for i, ticket in enumerate(other_tickets):
            if i in bad_idx:
                continue
            val = int(ticket.split(',')[idx])
            if not (bounds[0] <= val <= bounds[1] or bounds[2] <= val <= bounds[3]):
                possible_idxs.remove(idx)
                break
    rule_idxs[rule] = possible_idxs

while True:
    all_ints = True
    for rule in rule_idxs:
        if type(rule_idxs[rule]) == list:
#             if len(rule_idxs[rule]) == 1:
#                 idx = rule_idxs[rule][0]
#                 rule_idxs[rule] = idx
#                 for rule in rule_idxs:
#                     if type(rule_idxs[rule]) == list:
#                         try:
#                             rule_idxs[rule].remove(idx)
#                         except:
#                             pass
            all_ints = False
    idx_counts = {idx: (0, -1) for idx in idxs}
    for idx in idxs:
        count = idx_counts[idx][0]
        for rule in rule_idxs:
            if type(rule_idxs[rule]) != list:
                continue
            possible_idxs = rule_idxs[rule]
            if idx in possible_idxs:
                idx_counts[idx] = (count + 1, rule)
                count += 1
    for idx in idx_counts:
        if idx_counts[idx][0] == 1:
            rule_idxs[idx_counts[idx][1]] = idx
            for rule in rule_idxs:
                if type(rule_idxs[rule]) == list:
                    try:
                        rule_idxs[rule].remove(idx)
                    except:
                        pass
    if all_ints:
        break

prod = 1
for rule in rule_idxs:
    if rule.startswith('departure'):
        prod *= my_ticket[rule_idxs[rule]]

print(prod)
