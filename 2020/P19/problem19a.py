from re import fullmatch

data = open('problem19.txt', 'r').read().splitlines()

rules_end = data.index('')
rules = data[:rules_end]
strings = data[rules_end + 1:]

rules_list = ['' for i in range(134)]
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

regex_list = [None for i in range(134)]

def build_regex(idx):
    if regex_list[idx]:
        return regex_list[idx]
    rule = rules_list[idx]
    if type(rule) == str:
        regex_list[idx] = rule
        return rule
    elif type(rule) == list:
        ret = ''
        for ridx in rule:
            ret += '({})'.format(build_regex(ridx))
        regex_list[idx] = ret
        return ret
    elif type(rule) == tuple:
        r1 = ''
        for ridx in rule[0]:
            r1 += '({})'.format(build_regex(ridx))
        r1 = '({})'.format(r1)
        r2 = ''
        for ridx in rule[1]:
            r2 += '({})'.format(build_regex(ridx))
        r2 = '({})'.format(r2)
        ret = '{}|{}'.format(r1, r2)
        regex_list[idx] = ret
        return ret
    else:
        print("WTF?")

r0 = build_regex(0)

total = 0
for string in strings:
    if fullmatch(r0, string):
        total += 1

print(total)
