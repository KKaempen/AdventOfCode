data = []
with open("problem20.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [int(x) for x in data]

class ListNode():
    def __init__(self, val, num_nodes):
        self.val = val
        self.n = num_nodes
        self.next = None
        self.prev = None

    def cycle_node(self):
        v = self.val
        v %= self.n - 1
        new_prev = self.prev
        self.prev.next = self.next
        self.next.prev = self.prev
        for i in range(abs(v)):
            if v < 0:
                new_prev = new_prev.prev
            else:
                new_prev = new_prev.next
        new_next = new_prev.next
        self.next = new_next
        self.prev = new_prev
        new_prev.next = self
        new_next.prev = self

    def print(self):
        curr = self
        l = []
        while curr.next != self:
            l.append(curr.val)
            curr = curr.next
        l.append(curr.val)
        print(l)

nodes = []
curr = ListNode(data[0] * 811589153, len(data))
nodes.append(curr)
zero_node = None
for d in data[1:]:
    new_node = ListNode(d * 811589153, len(data))
    nodes.append(new_node)
    if d == 0:
        zero_node = new_node
    curr.next = new_node
    new_node.prev = curr
    curr = new_node

nodes[0].prev = nodes[-1]
nodes[-1].next = nodes[0]

for i in range(10):
    for n in nodes:
        n.cycle_node()

total = 0
curr = zero_node
#l = []
#for i in range(len(nodes)):
#    l.append(curr.val)
#    curr = curr.next
#print(l)
#print(l[1000])
#print(l[2000])
#print(l[3000])
#curr = zero_node
for i in range(3000):
    curr = curr.next
    if (i + 1) % 1000 == 0:
        print("At i =", i + 1)
        print("Val is", curr.val)
        print()
        total += curr.val

print(total)
