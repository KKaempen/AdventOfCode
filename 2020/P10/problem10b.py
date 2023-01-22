data = [int(x) for x in open('problem10.txt', 'r').read().splitlines()] + [0]

data.sort()
data.append(data[len(data) - 1] + 3)

nums = [1]
for i in range(1, len(data)):
    d = data[i]
    i1 = i - 1 if i - 1 >= 0 and d - data[i - 1] <= 3 else -1
    i2 = i - 2 if i - 2 >= 0 and d - data[i - 2] <= 3 else -1
    i3 = i - 3 if i - 3 >= 0 and d - data[i - 3] <= 3 else -1
    nums.append(0)
    for j in [i1, i2, i3]:
        if j != -1:
            nums[i] += nums[j]

print(nums[len(nums) - 1])
