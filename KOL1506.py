for _ in range(int(input())):
    ans = 0
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            val = abs(a[i] - a[j])
            val = val ** k
            ans += val
    ans = 2 * ans
    print(ans % 1000000007)

    # TLE Occurring
    # Fix it
