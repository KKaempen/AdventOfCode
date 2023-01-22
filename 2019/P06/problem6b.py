data = []
with open("problem6.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

orbits = {}
for d in data:
    ob1, ob2 = d.split(')')
    orbits[ob2] = ob1

curr_obj = orbits["SAN"]
santa_orbs = {}
dist = 0
while curr_obj in orbits:
    santa_orbs[curr_obj] = dist
    curr_obj = orbits[curr_obj]
    dist += 1

curr_obj = orbits["YOU"]
dist = 0
while curr_obj in orbits:
    if curr_obj in santa_orbs:
        dist += santa_orbs[curr_obj]
        break
    else:
        dist += 1
        curr_obj = orbits[curr_obj]

print(dist)
