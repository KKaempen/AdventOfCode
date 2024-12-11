from collections import defaultdict

data = []
with open("problem11.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

stones = data[0].split()
stone_dict = defaultdict(int)
for stone in stones:
    stone_dict[stone] += 1

for i in range(25):
    new_stone_dict = defaultdict(int)
    for stone, count in stone_dict.items():
        if stone == '0':
            new_stone_dict['1'] += count
        elif len(stone) % 2 == 0:
            half1 = str(int(stone[:len(stone) // 2]))
            half2 = str(int(stone[len(stone) // 2:]))
            new_stone_dict[half1] += count
            new_stone_dict[half2] += count
        else:
            next_val = str(int(stone) * 2024)
            new_stone_dict[next_val] += count
    stone_dict = new_stone_dict

print(sum(stone_dict.values()))
