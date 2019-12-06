orbits = {}
while True:
    try:
        stuff = input("")
        orb = stuff.split(")")
        orbits[orb[1].strip()] = orb[0].strip()
    except:
        break

start = orbits["YOU"]
finish = orbits["SAN"]
santa_orbs = {}
dist = 0
cur = finish
while cur in orbits:
    santa_orbs[cur] = dist
    cur = orbits[cur]
    dist += 1

cur = start
dist = 0
while cur in orbits:
    if cur in santa_orbs:
        print("Total: " + str(dist + santa_orbs[cur]))
        break
    else:
        dist += 1
        cur = orbits[cur]
