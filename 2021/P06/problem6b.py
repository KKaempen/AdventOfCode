data = open("problem6.txt", 'r').readlines()[0].strip()
data = [int(x) for x in data.split(',')]

fish = [0 for i in range(9)]

for d in data:
    fish[d] += 1

for i in range(256):
    new_fish = fish[0]
    for i in range(0, 6):
        fish[i] = fish[i + 1]
    fish[6] = fish[7] + new_fish
    fish[7] = fish[8]
    fish[8] = new_fish

print(sum(fish))
