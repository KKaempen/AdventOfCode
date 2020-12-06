print(max([int(d.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for d in open('problem5.txt', 'r').read().splitlines()]))
