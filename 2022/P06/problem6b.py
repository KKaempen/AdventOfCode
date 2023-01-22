data = []
with open("problem6.txt", 'r') as f:
    data = f.read()

seen = []
for i in range(14):
    seen.append(data[i])
idx = -1
for i in range(14, len(data)):
    if len(set(seen)) == 14:
        idx = i
        break
    else:
        seen.pop(0)
        seen.append(data[i])

print(idx)
