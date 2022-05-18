import sys

n = int(sys.stdin.readline().rstrip())
listn = [0] * 10001

for _ in range(n):
    listn[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    if listn[i] != 0:
        for _ in range(listn[i]):
            print(i)