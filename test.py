f = open("Resources/problem7.txt")
nums = f.read().split(",")
a = []
for b in nums:
    a.append(int(b))

print(a)
print(a[118:])
print(a[199:])
print(a[280:])
print(a[361:])
print(a[442:])
