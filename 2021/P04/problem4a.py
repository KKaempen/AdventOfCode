data = [s.strip() for s in open("problem4.txt", 'r').readlines()]

nums = [int(x) for x in data[0].split(',')]
chunks = []
i = 2
while True:
    new_chunk = []
    while i < len(data) and data[i] != '':
        new_chunk.append(data[i])
        i += 1
    i += 1
    chunks.append(new_chunk)
    if i >= len(data):
        break

def string_to_arr(s):
    a = []
    for x in s.split():
        if x != '':
            a.append(int(x))
    return a

def get_bingo_tuples(board):
    s = set({})
    for i in range(5):
        t1 = tuple(sorted(board[i]))
        t2 = tuple(sorted([board[j][i] for j in range(5)]))
        s.add(t1)
        s.add(t2)
#    s.add(tuple(sorted([board[i][i] for i in range(5)])))
#    s.add(tuple(sorted([board[i][5 - i - 1] for i in range(5)])))
    return s

chunks = [[string_to_arr(s) for s in chunk] for chunk in chunks]
all_bingo_tuples = {}
for i, board in enumerate(chunks):
    bingo_tuples = get_bingo_tuples(board)
    for t in bingo_tuples:
        all_bingo_tuples[t] = i

called_numbers = set({})
answer = -1
for num in nums:
    called_numbers.add(num)
    for t in all_bingo_tuples:
        if set(t).issubset(called_numbers):
            board_val = sum([sum([y for y in x if y not in called_numbers]) for x in chunks[all_bingo_tuples[t]]])
            answer = board_val * num
            break
    if answer >= 0:
        break

print(answer)
