for i in range(int(input())):
    n, k = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    weights = sorted(weights)
    boy, chef = 0, 0
    if k > n // 2:
        for _ in range(n - k, n):
            boy += weights[_]
        for j in range(n - k):
            chef += weights[j]
        print(boy - chef)
        continue
    else:
        for _ in range(k):
            boy += weights[_]
        for j in range(k, len(weights)):
            chef += weights[j]
        print(chef - boy)
        continue
