data = []
with open("problem8.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = data[0]
layers = [data[150 * x: 150 * (x + 1)] for x in range(len(data) // 150)]

min_zeros = 151
best_idx = -1
for i, l in enumerate(layers):
    num_zeros = l.count('0')
    if num_zeros < min_zeros:
        min_zeros = num_zeros
        best_idx = i

l = layers[best_idx]
print(l.count('1') * l.count('2'))
