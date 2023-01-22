data = []
with open("problem5.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data2 = '\n'.join(data).split('\n\n')
stacks = data2[0].split('\n')
instructions = data2[1].strip().split('\n')
stack_num = len(stacks[-1].strip().split('   '))
stack_arrs = [[] for i in range(stack_num)]
for i in range(len(stacks) - 2, -1, -1):
    for j in range(stack_num):
        new_char = stacks[i][4 * j + 1]
        if new_char != ' ':
            stack_arrs[j].append(new_char)

for inst in instructions:
    parsed_inst = [int(x) for x in inst.replace('move ', '').replace('from', 'to').split(' to ')]
    num = parsed_inst[0]
    f = parsed_inst[1] - 1
    t = parsed_inst[2] - 1
    moved_stack = []
    for i in range(num):
        c = stack_arrs[f].pop()
        moved_stack.append(c)
    for i in range(num):
        c = moved_stack.pop()
        stack_arrs[t].append(c)

s = ''.join([stack_arrs[i][-1] for i in range(stack_num)])
print(s)
