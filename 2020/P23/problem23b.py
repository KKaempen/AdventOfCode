cups = [int(x) for x in open('problem23.txt', 'r').read().splitlines()[0]]

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = self

class CircleLinkedList:
    def __init__(self, l):
        self.cur = ListNode(l[0])
        self.refs = [None for i in range(len(l))]
        self.refs[self.cur.val - 1] = self.cur
        last_node = self.cur
        for i, x in enumerate(l[1:]):
            node = ListNode(x)
            self.refs[x - 1] = node
            last_node.next = node
            if i == len(l) - 2:
                node.next = self.cur
            last_node = node
        self.n = len(l)

    def print(self):
        c = self.cur
        print('[', end='')
        print(c.val, end='')
        c = c.next
        while c != self.cur:
            print(',', c.val, end='')
            c = c.next
        print(']')

    def find(self, val):
        if val > len(self.refs):
            raise Exception("Value not found")
        return self.refs[val - 1]

    def iterate(self):
        n = self.n
        cur = self.cur
        dest = (cur.val - 2) % n + 1
        next_vals = []
        next_1 = cur.next
        to_add = cur
        for i in range(3):
            to_add = to_add.next
            next_vals.append(to_add.val)
        cur.next = to_add.next
        while dest in next_vals:
            dest = (dest - 2) % n + 1
        d = self.find(dest)
        to_add.next = d.next
        d.next = next_1
        self.cur = cur.next 

n = len(cups)
for i in range(n + 1, 1000001):
    cups.append(i)

l = CircleLinkedList(cups)

for i in range(10000000):
    l.iterate()

one_loc = l.find(1)
print(one_loc.next.val * one_loc.next.next.val)
