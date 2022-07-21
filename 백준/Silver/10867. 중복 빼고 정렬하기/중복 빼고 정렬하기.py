import sys

n = int(sys.stdin.readline().rstrip())

count = list(map(int, sys.stdin.readline().split()))
result = set(count)
result = sorted(list(result))

for s in result:
    print(s, end=' ')
