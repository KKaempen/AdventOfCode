data = []
with open("problem2.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

count = 0
for line in data:
    report = [int(x) for x in line.split()]
    sames = {i for i in range(len(report) - 1) if report[i] == report[i + 1]}
    ups = {i for i in range(len(report) - 1) if report[i] < report[i + 1]}
    downs = {i for i in range(len(report) - 1) if report[i] > report[i + 1]}
    bigs = {i for i in range(len(report) - 1) if abs(report[i] - report[i + 1]) > 3}
    smaller = sames | ups | bigs if len(sames | ups | bigs) <= 2 else sames | downs | bigs
    added_one = False
    if len(smaller) == 0:
        count += 1
        added_one = True
    elif len(smaller) == 1:
        [idx] = smaller
        new_report1 = report[:idx] + report[idx + 1:]
        new_report2 = report[:idx + 1] + report[idx + 2:]
        if (
            all(x < y for x, y in zip(new_report1[:-1], new_report1[1:])) or
            all(x > y for x, y in zip(new_report1[:-1], new_report1[1:]))
            ) and all(abs(x - y) <= 3 for x, y in zip(new_report1[:-1], new_report1[1:])):
            count += 1
            added_one = True
        elif (
            all(x < y for x, y in zip(new_report2[:-1], new_report2[1:])) or
            all(x > y for x, y in zip(new_report2[:-1], new_report2[1:]))
            ) and all(abs(x - y) <= 3 for x, y in zip(new_report2[:-1], new_report2[1:])):
            count += 1
            added_one = True
    elif len(smaller) == 2:
        [idx1, idx2] = smaller
        idx = max(idx1, idx2)
        new_report = report[:idx] + report[idx + 1:]
        if (
            all(x < y for x, y in zip(new_report[:-1], new_report[1:])) or
            all(x > y for x, y in zip(new_report[:-1], new_report[1:]))
            ) and all(abs(x - y) <= 3 for x, y in zip(new_report[:-1], new_report[1:])):
            count += 1
            added_one = True


print(count)
