for _ in range(int(input())):
    no_of_horses = int(input())
    strength = list(map(int, input().split()))
    strength.sort()
    q = {}
    for i in range(len(strength) - 1):
        q[i] = abs(strength[i+1] - strength[i])
    print(min(q.values()))
