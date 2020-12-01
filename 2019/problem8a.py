data = input("")
min_zeros = 150
best_idx = 0
idx = 0
while idx < len(data) - 150:
    zeros = 0
    for i in range(150):
        if data[idx + i] == '0':
            zeros += 1
    if zeros < min_zeros:
        min_zeros = zeros
        best_idx = idx
    idx += 150

num1s = 0
num2s = 0
for i in range(150):
    if data[best_idx + i] == '1':
        num1s += 1
    elif data[best_idx + i] == '2':
        num2s += 1

print("Product: " + str(num1s * num2s))
