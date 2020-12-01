inst_str1 = input("")
inst_str2 = input("")
wire1 = inst_str1.split(",")
wire2 = inst_str2.split(",")

for i in range(len(wire1)):
    s = wire1[i]
    wire1[i] = (s[0], int(s[1:]))

for i in range(len(wire2)):
    s = wire2[i]
    wire2[i] = (s[0], int(s[1:]))

wire1_points = set({})
x = 0
y = 0
for inst in wire1:
    l = inst[1]
    for i in range(1, l + 1):
        if inst[0] == 'U':
            y = y + 1
        elif inst[0] == 'D':
            y = y - 1
        elif inst[0] == 'R':
            x = x + 1
        elif inst[0] == 'L':
            x = x - 1
        wire1_points.add((x, y))

both_points = set({})
x = 0
y = 0
for inst in wire2:
    l = inst[1]
    for i in range(1, l + 1):
        if inst[0] == 'U':
            y = y + 1
        elif inst[0] == 'D':
            y = y - 1
        elif inst[0] == 'R':
            x = x + 1
        elif inst[0] == 'L':
            x = x - 1
        if (x, y) in wire1_points:
            both_points.add((x, y))

m = -1
for point in both_points:
    new_m = abs(point[0]) + abs(point[1])
    if m == -1:
        m = new_m
    elif new_m < m:
        m = new_m

print("Minimum: " + str(m))
