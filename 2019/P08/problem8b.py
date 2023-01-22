data = []
with open("problem8.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = data[0]
layers = [data[150 * x: 150 * (x + 1)] for x in range(len(data) // 150)]

image = ""
for i in range(6):
    row = []
    for j in range(25):
        idx = 25 * i + j
        l = 0
        while layers[l][idx] == '2':
            l += 1
        row.append('O' if layers[l][idx] == '1' else ' ')
    image += ''.join(row) + '\n'

print(image)
