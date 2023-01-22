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
    if nums[1] == 1:
        round_score = (nums[0] - 1)
        if round_score == 0:
            round_score = 3
    elif nums[1] == 2:
        round_score = 3 + nums[0]
    elif nums[1] == 3:
        round_score = 6 + (nums[0] % 3) + 1
    score += round_score

print(score)
