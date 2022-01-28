import random

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b = map(int, input().split())
c = str(a - b)
j = ''
while True:
    new = random.choice(nums)
    if new == c[-1]:
        continue
    else:
        for _ in range(len(c) - 1):
            j += c[_]
        j += str(new)
        break
print(int(j))
