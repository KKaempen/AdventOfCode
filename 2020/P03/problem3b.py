trees = open('problem3.txt', 'r').read().split('\n')

def find_num_hit(over, down):
    num_hit = 0
    x = 0
    y = 0
    while y < len(trees):
        if trees[y][x] == '#':
            num_hit += 1
        x += over
        y += down
        x = x % len(trees[0])
    return num_hit

print(find_num_hit(1, 1) * find_num_hit(3, 1) * find_num_hit(5, 1) * find_num_hit(7, 1) * find_num_hit(1, 2))
