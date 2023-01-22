data = []
with open("problem9.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

def get_new_t_pos(h_pos, t_pos, v):
    d_x = h_pos[0] - t_pos[0]
    d_y = h_pos[1] - t_pos[1]
    if abs(d_x) == 2 and abs(d_y) == 1:
        t_pos = (t_pos[0] + d_x // abs(d_x), t_pos[1] + d_y)
    elif abs(d_x) >= 2:
        t_pos = (t_pos[0] + d_x // abs(d_x), t_pos[1])
    elif abs(d_x) >= 1 and abs(d_y) >= 2:
        t_pos = (t_pos[0] + d_x, t_pos[1] + d_y // abs(d_y))
    elif abs(d_y) >= 2:
        t_pos = (t_pos[0], t_pos[1] + d_y // abs(d_y))
    v.add(t_pos)
    return t_pos

visited = {(0, 0)}

h_pos = (0, 0)
t_pos = (0, 0)
for d in data:
    inst = d.split()
    if inst[0] == 'D':
        for i in range(int(inst[1])):
            h_pos = (h_pos[0], h_pos[1] - 1)
            t_pos = get_new_t_pos(h_pos, t_pos, visited)
    if inst[0] == 'U':
        for i in range(int(inst[1])):
            h_pos = (h_pos[0], h_pos[1] + 1) 
            t_pos = get_new_t_pos(h_pos, t_pos, visited)
    if inst[0] == 'L':
        for i in range(int(inst[1])):
            h_pos = (h_pos[0] - 1, h_pos[1])
            t_pos = get_new_t_pos(h_pos, t_pos, visited)
    if inst[0] == 'R':
        for i in range(int(inst[1])):
            h_pos = (h_pos[0] + 1, h_pos[1])
            t_pos = get_new_t_pos(h_pos, t_pos, visited)

print(len(visited))
