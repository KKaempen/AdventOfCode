data = input("")
min_zeros = 150
best_idx = 0
idx = 0
image = [[-1 for i in range(25)] for j in range(6)]
for i in range(25):
    for j in range(6):
        idx = 25 * j + i
        while data[idx] == '2':
            idx += 150
        image[j][i] = data[idx]
        
print("Image: ")
for i in range(6):
    s = ""
    for j in range(25):
        s += image[i][j] + " "
    print(s)
 
