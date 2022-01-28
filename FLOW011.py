for _ in range(int(input())):
    amount = int(input())
    if amount < 1500:
        grossAmount = amount + (amount / 10) + ((amount / 10) * 9)
    else:
        grossAmount = amount + 500 + ((amount / 10) * 9.8)

    print(grossAmount)
