import re

data = []
with open("problem3.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

total = 0
line = ''.join(data)
regex = re.compile('mul\(\d\d?\d?,\d\d?\d?\)')
matches = regex.findall(line)
for m in matches:
    nums = m[4: -1].split(',')
    num1 = int(nums[0])
    num2 = int(nums[1])
    total += num1 * num2

print(total)
