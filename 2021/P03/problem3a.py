data = [int(datum, 2) for datum in open("problem3.txt", 'r').readlines()]

num_ones = [0 for i in range(12)]
for d in data:
    for i in range(len(num_ones)):
        num_ones[i] += 1 if d & 2**i else 0

gamma = 0
epsilon = 0
for i in range(len(num_ones)):
    if num_ones[i] >= len(data) - num_ones[i]:
        epsilon += 2**i
    else:
        gamma += 2**i

print(epsilon * gamma)
