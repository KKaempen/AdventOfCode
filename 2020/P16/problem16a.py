data = open('problem16.txt', 'r').read().splitlines()

break1 = data.index('')
break2 = data.index('', break1 + 1)
rules = data[:break1]
my_ticket = data[break1 + 2:break2]
other_tickets = data[break2 + 2:]

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

total = 0
for ticket in other_tickets:
    vals = [int(x) for x in ticket.split(',')]
    for val in vals:
        for rule in rules_d:
            bounds = rules_d[rule]
            if bounds[0] <= val <= bounds[1] or bounds[2] <= val <= bounds[3]:
                break
        else:
            total += val

print(total)
