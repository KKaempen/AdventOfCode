from collections import defaultdict

data = []
with open("problem11.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

stones = [int(x) for x in data[0].split()]
stone_dict = defaultdict(int)
for stone in stones:
    stone_dict[stone] += 1

for i in range(75):
    new_stone_dict = defaultdict(int)
    for stone, count in stone_dict.items():
        if stone == 0:
            new_stone_dict[1] += count
        else:
            sqrt_nearest_10 = 1
            while sqrt_nearest_10 * sqrt_nearest_10 <= stone:
                sqrt_nearest_10 *= 10
            if stone * 10 >= sqrt_nearest_10 * sqrt_nearest_10:
                # Even length
                half1, half2 = divmod(stone, sqrt_nearest_10)
                new_stone_dict[half1] += count
                new_stone_dict[half2] += count
            else:
                new_stone_dict[stone * 2024] += count
    stone_dict = new_stone_dict

print(sum(stone_dict.values()))
