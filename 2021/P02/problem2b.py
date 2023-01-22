data = open("problem2.txt", 'r').readlines()

real_data = []
for d in data:
    s = d.split()
    real_data.append((s[0], int(s[1])))

h_pos = 0
v_pos = 0
aim = 0
for d in real_data:
    if d[0] == 'forward':
        h_pos += d[1]
        v_pos += d[1] * aim
    elif d[0] == 'up':
        aim -= d[1]
    elif d[0] == 'down':
        aim += d[1]

print(v_pos * h_pos)
