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
        if not possible[i]:
            continue
        for pattern in patterns:
            if design[i:].startswith(pattern):
                possible[i + len(pattern)] += possible[i]
    count += possible[-1]

print(count)
