def no_of_zeros_by_five(m):
    five_value = 0
    i = 1
    while True:
        if 5 ** i > m:
            break
        else:
            five_value += m // (5 ** i)
            i += 1
    return five_value


for _ in range(int(input())):
    print(no_of_zeros_by_five(int(input())))
