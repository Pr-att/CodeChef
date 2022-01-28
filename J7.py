for _ in range(int(input())):
    p, s = map(int, input().split())
    y2 = (p - (((p ** 2) - (4 * 6 * s)) ** (1 / 2))) / 12
    x2 = (s - (2 * y2 * y2)) / (4 * y2)
    first = round((x2 * y2 * y2), 2)
    print(first)
