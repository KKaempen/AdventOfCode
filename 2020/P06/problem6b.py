import string

data = open('problem6.txt', 'r').read().splitlines()

data = ' '.join(data).split('  ')

total = 0
for d in data:
    answers = d.split(' ')
    s = set(string.ascii_lowercase)
    for answer in answers:
        s = s.intersection(set(answer))
    total += len(s)

print(total)
