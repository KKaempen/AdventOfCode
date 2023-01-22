data = open('problem9.txt', 'r').read().splitlines()

nums = []
for i in range(25):
    nums.append(int(data[i]))

for i in range(26, len(data)):
    d = int(data[i])
    works = False
    for i, x in enumerate(nums):
        for y in nums[i + 1:]:
            if x + y == d:
                works = True
    if not works:
        print(d)
        break
    nums = nums[1:] + [d]

