data = []
with open("problem1.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data_s = ' '.join(data)
unfolded_arr = [[int(x) for x in s.split(' ')] for s in data_s.split('  ')]
sum_arr = [sum(a) for a in unfolded_arr]
sum_arr = sorted(sum_arr, reverse=True)
print(sum_arr[0] + sum_arr[1] + sum_arr[2])

#data = [int(x.strip()) if x != '\n' else x.strip() for x in data]
#cur_best1 = 0
#cur_best2 = 0
#cur_best3 = 0
#cur_total = 0
#for d in data:
#    if d == '':
#        if cur_total > cur_best1:
#            cur_best3 = cur_best2
#            cur_best2 = cur_best1
#            cur_best1 = cur_total
#        elif cur_total > cur_best2:
#            cur_best3 = cur_best2
#            cur_best2 = cur_total
#        elif cur_total > cur_best3:
#            cur_best3 = cur_total
#        cur_total = 0
#    else:
#        cur_total += d
#print(cur_best1 + cur_best2 + cur_best3)
