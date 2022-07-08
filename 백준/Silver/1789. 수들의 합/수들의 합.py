import sys

n = int(sys.stdin.readline().rstrip())
count = 1
total = 0
for i in range(1, n+1):
    total += i
    if total == n:
        break
    if total > n:
        count -= 1
        break
    count += 1
print(count)
