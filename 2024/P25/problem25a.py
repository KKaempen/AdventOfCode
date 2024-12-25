data = []
with open("problem25.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = '\n'.join(data).split('\n\n')
locks = []
keys = []
for item in data:
    a = item.split('\n')
    nums = [0 for i in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            if a[j][i] == '#':
                nums[i] += 1
    if a[0] == '#####':
        locks.append(nums)
    else:
        keys.append(nums)

total = 0
for lock in locks:
    for key in keys:
        for i in range(len(lock)):
            if lock[i] + key[i] > 7:
                break
        else:
            total += 1

print(total)
