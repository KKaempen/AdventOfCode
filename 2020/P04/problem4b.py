data = open('problem4.txt').read().splitlines()

alnum = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
digs = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
eyes = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

eval_byr = lambda x: len(x) == 4 and 1920 <= int(x) <= 2002
eval_iyr = lambda x: len(x) == 4 and 2010 <= int(x) <= 2020
eval_eyr = lambda x: len(x) == 4 and 2020 <= int(x) <= 2030
eval_hgt = lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76)
eval_hcl = lambda x: x[0] == '#' and len(x) == 7 and set(x[1:]).issubset(alnum)
eval_ecl = lambda x: x in eyes
eval_pid = lambda x: len(x) == 9 and set(x).issubset(digs)

s2 = {'byr': eval_byr, 
      'eyr': eval_eyr, 
      'iyr': eval_iyr, 
      'hgt': eval_hgt, 
      'hcl': eval_hcl, 
      'ecl': eval_ecl, 
      'pid': eval_pid
      }

batches = ' '.join(data).split('  ')
total = 0
for batch in batches:
    s = batch.split(' ')
    counts = {x: 0 for x in s2}
    works = True
    for e in s:
        tag = e.split(':')[0]
        if tag == 'cid':
            continue
        other = e.split(':')[1]
        counts[tag] += 1
        works = works and s2[tag](other)
    for k in counts:
        count = counts[k]
        works = works and count
    if works:
        total += 1

print(total)
