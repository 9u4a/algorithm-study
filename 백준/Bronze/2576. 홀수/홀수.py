import sys

result = []
for _ in range(7):
    n = int(sys.stdin.readline().rstrip())
    if n % 2 == 1:
        result.append(n)

if len(result) == 0:
    print(-1)

else:
    print(sum(result))
    print(min(result))

