data = []
with open("problem19.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

patterns, designs = '\n'.join(data).split('\n\n')
patterns = set(patterns.split(', '))
designs = designs.split('\n')

count = 0
for design in designs:
    possible = [False for i in range(len(design) + 1)]
    possible[0] = True
    for i in range(len(design)):
        if possible[i + 1]:
            continue
        for j in range(i, -1, -1):
            if design[j: i + 1] in patterns and possible[j]:
                possible[i + 1] = True
                break
    if possible[-1]:
        count += 1

print(count)
