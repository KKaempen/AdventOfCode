data = []
with open("problem2.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

def f(char):
    if char == 'A' or char == 'X':
        return 1
    if char == 'B' or char == 'Y':
        return 2
    if char == 'C' or char == 'Z':
        return 3

score = 0
for p in data:
    chars = p.split(' ')
    nums = [f(x) for x in chars]
    round_score = 0
    if nums[0] == nums[1]:
        round_score += 3
    elif (nums[1] - nums[0] + 2) % 3 == 0:
        round_score += 6
    score += nums[1] + round_score

print(score)
