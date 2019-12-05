num_t = input("")
total = 0

while True:
    num = int(num_t)
    part_total = 0
    next_fuel_bit = num // 3 - 2
    while next_fuel_bit > 0:
        part_total += next_fuel_bit
        next_fuel_bit = next_fuel_bit // 3 - 2
    total += part_total
    try:
        num_t = input("")
        if num_t == "":
            break
    except:
        break

print("Total: " + str(total))
