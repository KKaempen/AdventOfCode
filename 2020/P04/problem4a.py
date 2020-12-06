data = open('problem4.txt').read().splitlines()

s1 = {'byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
s2 = {'byr', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid'}

batches = ' '.join(data).split('  ')
total = 0
for batch in batches:
    s = batch.split(' ')
    print(s)
    tags = set({})
    for e in s:
        tags.add(e.split(':')[0])
    print(tags)
    if s2.issubset(tags):
        total += 1

print(total)
