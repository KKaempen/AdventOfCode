data = []
with open("problem7.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

def can_make(result, rest):
    if len(rest) == 1:
        return rest[0] == result

    last = rest[-1]

    if result % last == 0:
        possible_mul = can_make(result // last, rest[:-1])
    else:
        possible_mul = False

    next_power_of_10 = 1
    while next_power_of_10 <= last:
        next_power_of_10 *= 10
    if (result - last) % next_power_of_10 == 0:
        possible_concat = can_make((result - last) // next_power_of_10, rest[:-1])
    else:
        possible_concat = False

    possible_add = can_make(result - last, rest[:-1])
    return possible_mul or possible_add or possible_concat

total = 0
for line in data:
    result, rest = line.split(': ')
    result = int(result)
    rest = [int(x) for x in rest.split()]
    if can_make(result, rest):
        total += result

print(total)
