import string

data = open('problem6.txt', 'r').read().splitlines()

data = ' '.join(data).split('  ')

total = 0
for d in data:
    total += len(set(d.replace(' ', '')))

print(total)
