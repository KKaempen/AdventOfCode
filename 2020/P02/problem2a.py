lines = open('problem2.txt', 'r').readlines()

total = 0

for l in lines:
    d = l.split(': ')
    nums = d[0].split(' ')[0]
    lo = int(nums.split('-')[0])
    hi = int(nums.split('-')[1])
    password = d[1]
    c = d[0].split(' ')[1]
    if lo <= password.count(c) <= hi:
        total += 1

print(total)
