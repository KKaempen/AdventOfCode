import re

data = []
with open("problem3.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

total = 0
do = True
for line in data:
    main_regex = re.compile('mul\(\d\d?\d?,\d\d?\d?\)')
    do_regex = re.compile('do\(\)')
    dont_regex = re.compile('don\'t\(\)')

    main_matches = list(main_regex.finditer(line))
    do_matches = list(do_regex.finditer(line))
    dont_matches = list(dont_regex.finditer(line))

    main_idx = 0
    do_idx = 0
    dont_idx = 0
    while main_idx + do_idx + dont_idx < len(main_matches) + len(do_matches) + len(dont_matches):
        main_match = main_matches[main_idx] if main_idx < len(main_matches) else None
        do_match = do_matches[do_idx] if do_idx < len(do_matches) else None
        dont_match = dont_matches[dont_idx] if dont_idx < len(dont_matches) else None

        main_pos = main_match.start() if main_match else len(line)
        do_pos = do_match.start() if do_match else len(line)
        dont_pos = dont_match.start() if dont_match else len(line)

        if main_pos == min(main_pos, do_pos, dont_pos):
            if do:
                m = main_match.group(0)
                nums = m[4: -1].split(',')
                num1 = int(nums[0])
                num2 = int(nums[1])
                total += num1 * num2
            main_idx += 1
        if do_pos == min(main_pos, do_pos, dont_pos):
            do = True
            do_idx += 1
        if dont_pos == min(main_pos, do_pos, dont_pos):
            do = False
            dont_idx += 1

print(total)
