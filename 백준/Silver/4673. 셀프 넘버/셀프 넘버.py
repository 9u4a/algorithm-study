def d(n):
    dn = 0
    if n < 10:
        dn = n + n
    elif 9 < n < 100:
        dn = n + int(n / 10) + int(n % 10)
    elif 99 < n < 1000:
        dn = n + int(n / 100) + int((n / 10) % 10) + int(n % 10)
    elif 999 < n < 10000:
        dn = n + int(n / 1000) + int((n / 100) % 10) + int((n / 10) % 10) + int(n % 10)
    elif n == 10000:
        dn = 10001
    return dn


numtoMax = set(range(1, 10001))
notSelfNum = set()

for i in range(1, 10001):
    n = d(i)
    if not n == 0:
        notSelfNum.add(d(i))

selfNum = sorted(numtoMax - notSelfNum)

for i in selfNum:
    print(i)
