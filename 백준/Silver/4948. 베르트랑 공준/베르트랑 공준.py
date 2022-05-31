def prime(n):
    if (n < 2):
        return 0
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return 0
        i += 1
    return 1

p = []
for i in range(2, 2 * 123456 + 1):
    if (prime(i) == 1):
        p.append(i)

while (True):
    n = int(input())
    if (n == 0):
        break
    cnt = 0
    for i in p:
        if (n < i and i <= 2*n):
            cnt += 1
    print(cnt)