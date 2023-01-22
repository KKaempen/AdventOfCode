data = []
with open('problem25.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')

c_k = int(data[0])
d_k = int(data[1])

t = 1
num = 0
c_l = -1
d_l = -1
while True:
    num += 1
    t *= 7
    t %= 20201227
    if t == c_k and c_l == -1:
        c_l = num
    if t == d_k and d_l == -1:
        d_l = num
    if c_l != -1 and d_l != -1:
        break

t = 1
for i in range(d_l):
    t *= c_k
    t %= 20201227

print(t)

