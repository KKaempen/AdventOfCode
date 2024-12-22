from collections import defaultdict

data = []
with open("problem21.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

num_pad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A'],
]
num_pad_dict = {c: (i, j) for i, row in enumerate(num_pad) for j, c in enumerate(row)}
direc_pad = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]
direc_pad_dict = {c: (i, j) for i, row in enumerate(direc_pad) for j, c in enumerate(row)}

def get_dir(cx, cy, nx, ny, dx, dy, numpad):
    next_dir = None
    if dx == 0:
        next_dir = ('<',) if dy < 0 else ('>',)
    elif dy == 0:
        next_dir = ('^',) if dx < 0 else ('v',)
    elif numpad and cx == 3 and ny == 0:
        next_dir = ('^', '<')
    elif numpad and cy == 0 and nx == 3:
        next_dir = ('>', 'v')
    elif not numpad and cx == 0 and ny == 0:
        next_dir = ('v', '<')
    elif not numpad and cy == 0 and nx == 0:
        next_dir = ('>', '^')
    elif dy < 0:
        next_dir = ('<', '^') if dx < 0 else ('<', 'v')
    elif dx > 0:
        next_dir = ('v', '<') if dy < 0 else ('v', '>')
    else:
        next_dir = ('^', '>')
    return next_dir

for code in data:
    instructions = defaultdict(int)
    int_part = int(code.replace('A', ''))
    curr_button = 'A'
    for key in code:
        cx, cy = num_pad_dict[curr_button]
        nx, ny = num_pad_dict[key]
        dx, dy = (nx - cx, ny - cy)
        next_dir = get_dir(cx, cy, nx, ny, dx, dy, True)
        instructions[next_dir] += abs(dx) + abs(dy) + 1
        curr_button = key

    for _ in range(2):
        next_instructions = defaultdict(int)
        for instruction, presses in instructions.items():
            curr_button = 'A'
            instruction += ('A',)
            for direc in instruction:
                cx, cy = num_pad_dict[curr_button]
                nx, ny = num_pad_dict[direc]
                dx, dy = (nx - cx, ny - cy)
                next_dir = get_dir(cx, cy, nx, ny, dx, dy, False)
                next_instructions[next_dir] += abs(dx) + abs(dy) + 1
                curr_button = key
