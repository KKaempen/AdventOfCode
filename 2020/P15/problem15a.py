data = [int(x) for x in open('problem15.txt', 'r').read().splitlines()[0].split(',')]

last_spoken = 0
spoken = {}
spoken_diff = -1
for i in range(2020):
    if i < len(data):
        last_spoken = data[i]
        spoken[last_spoken] = i
    else:
        if spoken_diff == -1:
            last_spoken = 0
        else:
            last_spoken = spoken_diff
        if last_spoken in spoken:
            spoken_diff = i - spoken[last_spoken]
        else:
            spoken_diff = -1
        spoken[last_spoken] = i

print(last_spoken)
