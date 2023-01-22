data = []
with open("problem6.txt", 'r') as f:
    data = f.read()

seen = []
seen.append(data[0])
seen.append(data[1])
seen.append(data[2])
seen.append(data[3])
idx = -1
for i in range(4, len(data)):
    if len(set(seen)) == 4:
        idx = i
        break
    else:
        seen.pop(0)
        seen.append(data[i])

print(idx)
