orbits = {}
while True:
    try:
        stuff = input("")
        orb = stuff.split(")")
        orbits[orb[1].strip()] = orb[0].strip()
    except:
        break

total_num = 0
for orb in orbits:
    curr_num = 0
    while orb in orbits:
        curr_num += 1
        orb = orbits[orb]
    total_num += curr_num

print("Total: " + str(total_num))
