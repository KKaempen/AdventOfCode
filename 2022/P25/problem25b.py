from math import log

data = []
with open("problem25.txt", 'r') as f:
    data = f.read().strip('\n').split('\n')

digits = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
total = 0
for d in data:
    place = 1
    val = 0
    for a in d[::-1]:
        val += place * digits[a]
        place *= 5
    total += val

digits_inv = {digits[x]: x for x in digits}
negative_map = {"2": "=", "1": "-", "0": "0", "-": "1", "=": "2"}
log_half = 1 + log(1/2, 5)
def get_snafu_val(num):
    if num == 0:
        return ""
    m1 = num % 5
    m1 = ((m1 + 2) % 5) - 2
    d0 = digits_inv[m1]
    rest = get_snafu_val((num - m1) // 5)
    rest += d0
    return rest

print("Merry Christmas!")#get_snafu_val(total))
