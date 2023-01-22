data = open('problem19.txt', 'r').read().splitlines()

rules_end = data.index('')
rules = data[:rules_end]
strings = data[rules_end + 1:]
max_rule = -1
for rule in rules:
    max_rule = max(max_rule, int(rule.split(': ')[0]))

rules_list = ['' for i in range(max_rule + 1)]
for rule in rules:
    rule_idx = int(rule.split(': ')[0])
    rule_def = rule.split(': ')[1]
    if '|' in rule_def:
        p1 = rule_def.split(' | ')[0]
        p2 = rule_def.split(' | ')[1]
        p1 = [int(x) for x in p1.split()]
        p2 = [int(x) for x in p2.split()]
        rules_list[rule_idx] = (p1, p2)
    elif '"' in rule_def:
        rules_list[rule_idx] = rule_def.replace('"', '')
    else:
        rules_list[rule_idx] = [int(x) for x in rule_def.split()]

for i, rule in enumerate(rules_list):
    if rule == '':
        rules_list[i] = 'a'

eight_tup = ([42, 8],)
if type(rules_list[42]) == tuple:
    for l in rules_list[42]:
        eight_tup += (l,)
else:
    eight_tup += (rules_list[42],)

eleven_tup = ([42, 31], [42, len(rules_list)])
add_tup = [11, 31]
rules_list[8] = eight_tup
rules_list[11] = eleven_tup
rules_list.append(add_tup)

for i, r in enumerate(rules_list):
    if type(r) == list and len(r) == 1:
        rules_list[i] = rules_list[r[0]]
    if type(r) == tuple:
        new_tup = ()
        for l in r:
            if len(l) == 1:
                add_tup = rules_list[l[0]]
                add_tup = add_tup if type(add_tup) == tuple else (add_tup,)
                new_tup += add_tup
            else:
                new_tup += (l,)
        rules_list[i] = new_tup

def match(string, rules_list):
    matches = [[[False for i in range(len(rules_list))] for j in range(len(string))] for k in range(len(string))]
    for s in range(len(string)):
        for i, r in enumerate(rules_list):
            if type(r) == str and r == string[s]:
                matches[0][s][i] = True
            elif type(r) == tuple:
                for t in r:
                    if type(t) == str and t == string[s]:
                        matches[0][s][i] = True
    for l in range(2, len(string) + 1):
        for s in range(1, len(string) - l + 2):
            for p in range(1, l):
                for i, r in enumerate(rules_list):
                    if type(r) != str:
                        t = (r,) if type(r) == list else r
                        for rule in t:
                            if type(rule) == str:
                                continue
                            matches[l - 1][s - 1][i] |= (matches[p - 1][s - 1][rule[0]] and matches[l - p - 1][s + p - 1][rule[1]])

    return matches[len(string) - 1][0][0]

total = 0
num = 0
for string in strings:
    num += 1
    if match(string, rules_list):
        total += 1

print(total)
