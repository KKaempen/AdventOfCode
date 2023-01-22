data = []
with open("problem1.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data_s = ' '.join(data)
unfolded_arr = [[int(x) for x in s.split(' ')] for s in data_s.split('  ')]
sum_arr = [sum(a) for a in unfolded_arr]
print(max(sum_arr))

#data = [int(x.strip()) if x != '\n' else x.strip() for x in data]
#cur_best = 0
#cur_total = 0
#for d in data:
#    if d == '':
#        cur_best = max(cur_best, cur_total)
#        cur_total = 0
#    else:
#        cur_total += d
#print(cur_best)
