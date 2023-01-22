data = []
with open("problem6.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

orbits = {}
for d in data:
    ob1, ob2 = d.split(')')
    orbits[ob2] = ob1

total_num = 0
for orb in orbits:
    temp = orb
    while temp in orbits:
        total_num += 1
        temp = orbits[temp]

print(total_num)
