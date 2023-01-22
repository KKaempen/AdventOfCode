data = []
with open("problem1.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data]

total = 0
for d in data:
    next_fuel_bit = d // 3 - 2
    while next_fuel_bit > 0:
        total += next_fuel_bit
        next_fuel_bit = next_fuel_bit // 3 - 2

print(total)
