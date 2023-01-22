data = []
with open("problem8.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = [[int(x) for x in s] for s in data]
n = len(data)

best_score = 0

for i in range(n):
    for j in range(n):
        curr_height = data[i][j]
        see_left = 0
        see_right = 0
        see_up = 0
        see_down = 0
        k = 1
        while j - k > -1:
            see_left += 1
            if data[i][j - k] >= curr_height:
                break
            k += 1
        k = 1
        while j + k < n:
            see_right += 1
            if data[i][j + k] >= curr_height:
                break
            k += 1
        k = 1
        while i - k > -1:
            see_up += 1
            if data[i - k][j] >= curr_height:
                break
            k += 1
        k = 1
        while i + k < n:
            see_down += 1
            if data[i + k][j] >= curr_height:
                break
            k += 1
        prod = see_left * see_right * see_up * see_down
        if prod > best_score:
            best_score = prod 

print(best_score)
