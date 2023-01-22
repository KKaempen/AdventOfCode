data = []
with open("problem13.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

data = '\n'.join(data).split('\n\n')
data = [x.split('\n') for x in data]

def extract_bracket_items(s):
    idx = 0
    items = []
    while idx < len(s):
        if s[idx] == '[':
            j = 0
            b_count = 1
            while b_count > 0:
                j += 1
                if s[idx + j] == '[':
                    b_count += 1
                elif s[idx + j] == ']':
                    b_count -= 1
            items.append(s[idx: idx + j + 1])
            idx = idx + j + 2
        else:
            try:
                comma = s.index(',', idx)
                items.append(s[idx: comma])
                idx = comma + 1
            except:
                int_s = s[idx: -1] if s[-1] == ']' else s[idx:]
                items.append(int_s)
                idx = len(s)
    return items

def transform_to_list(s):
    if s[0] == '[':
        inner = s[1:-1]
        if inner == '':
            return []
        else:
            list_items = extract_bracket_items(inner)
            list_form = [transform_to_list(x) for x in list_items]
            return list_form
    else:
        return int(s)

data = [[transform_to_list(x[0]), transform_to_list(x[1])] for x in data]

def int_compare(p1, p2):
    ret_val = None
    if type(p1) == int and type(p2) == int:
        ret_val = 0 if p1 == p2 else 1 if p1 < p2 else -1
    if type(p1) == int:
        p1 = [p1]
    if type(p2) == int:
        p2 = [p2]
    return p1, p2, ret_val

def compare(p1, p2):
    stack = [(p1, p2)]
    while len(stack) > 0:
        item1, item2 = stack.pop()
#        print("Comparing", item1, "and", item2)
        item1, item2, ret_val = int_compare(item1, item2)
        if ret_val == 0:
            continue
        if ret_val:
            return ret_val
        if len(item1) == 0 and len(item2) == 0:
            continue
        if len(item1) == 0:
            return 1
        if len(item2) == 0:
            return -1
        sub_item1 = item1[0]
        sub_item2 = item2[0]
        next_item1 = item1[1:]
        next_item2 = item2[1:]
        stack.append((next_item1, next_item2))
        stack.append((sub_item1, sub_item2))
    return 0

tot = 0
for i, d in enumerate(data):
    res = compare(d[0], d[1])
#    print("Comparison result was", res)
    if res >= 0:
        tot += i + 1
#    print()

print(tot)
