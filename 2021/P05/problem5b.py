data = [s.strip() for s in open("problem5.txt", 'r').readlines()]

lines = []
for d in data:
    s = d.split(' -> ')
    p1 = s[0]
    p2 = s[1]
    s1 = p1.split(',')
    s2 = p2.split(',')
    t1 = (int(s1[0]), int(s1[1]))
    t2 = (int(s2[0]), int(s2[1]))
    lines.append((t1, t2))

points = {}
for l in lines:
    if l[0][0] == l[1][0]:
        p1 = min(l[0][1], l[1][1])
        p2 = max(l[0][1], l[1][1])
        for i in range(p1, p2 + 1):
            p = (l[0][0], i)
            if p not in points:
                points[p] = 0
            points[p] += 1
        continue
    if l[0][1] == l[1][1]:
        p1 = min(l[0][0], l[1][0])
        p2 = max(l[0][0], l[1][0])
        for i in range(p1, p2 + 1):
            p = (i, l[0][1])
            if p not in points:
                points[p] = 0
            points[p] += 1
        continue
    xdir = 0
    ydir = 0
    if l[0][0] < l[1][0]:
        xdir = 1
    else:
        xdir = -1
    if l[0][1] < l[1][1]:
        ydir = 1
    else:
        ydir = -1
    d = abs(l[0][0] - l[1][0])
    for i in range(d + 1):
        p = (l[0][0] + i * xdir, l[0][1] + i * ydir)
        if p not in points:
            points[p] = 0
        points[p] += 1

print(len([x for x in points if points[x] > 1]))
