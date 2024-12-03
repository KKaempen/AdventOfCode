import re

data = []
with open("problem3.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

total = 0
do = True
for line in data:
    regex = re.compile('mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)')

    matches = regex.findall(line)
    for match in matches:
        if match == 'do()':
            do = True
        elif match == 'don\'t()':
            do = False
        elif do:
            nums = match[4: -1].split(',')
            num1 = int(nums[0])
            num2 = int(nums[1])
            total += num1 * num2

print(total)
