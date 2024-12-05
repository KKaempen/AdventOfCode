from collections import defaultdict

data = []
with open("problem5.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = ('.'.join(data)).split('..')
rules = data[0]
tests = data[1]

rule_dict = defaultdict(list)
for rule in rules.split('.'):
    p1, p2 = rule.split('|')
    rule_dict[p1].append(p2)

count = 0
for test in tests.split('.'):
    pages = test.split(',')
    for p1, p2 in zip(pages[:-1], pages[1:]):
        if p2 not in rule_dict[p1]:
            break
    else:
        count += int(pages[len(pages) // 2])

print(count)



