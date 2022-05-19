import sys

n = int(sys.stdin.readline().rstrip())
divn = n
if n != 1:
    for i in range(2, n + 1):
        while divn % i == 0:
            divn /= i
            print(i)