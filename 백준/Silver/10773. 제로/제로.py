import sys

k = int(sys.stdin.readline().rstrip())
klist = []
for _ in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        klist.pop()
    else:
        klist.append(num)

print(sum(klist))
