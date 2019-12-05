num_t = input("")
total = 0

while True:
    num = int(num_t)
    total += num // 3 - 2
    try:
        num_t = input("")
        if num_t == "":
            break
    except:
        break

print("Total: " + str(total))
