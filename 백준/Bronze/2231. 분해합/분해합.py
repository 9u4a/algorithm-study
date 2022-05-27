import sys

n = int(sys.stdin.readline().rstrip())
result = 0
count = 0
for i in range(n):
    result = sum(map(int, str(i))) + i
    if result == n:
        count = i
        break
print(count)