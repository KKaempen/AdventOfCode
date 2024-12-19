data = []
with open("problem19.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

patterns, designs = '\n'.join(data).split('\n\n')
patterns = set(patterns.split(', '))
designs = designs.split('\n')

count = 0
for design in designs:
    possible = [0 for i in range(len(design) + 1)]
    possible[0] = 1
    for i in range(len(design)):
        for j in range(i, -1, -1):
            if design[j:i + 1] in patterns:
                possible[i + 1] += possible[j]
    count += possible[-1]

print(count)
