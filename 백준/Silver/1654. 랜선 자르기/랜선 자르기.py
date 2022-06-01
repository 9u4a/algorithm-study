import sys

k, n = map(int, sys.stdin.readline().split())
klist = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
start = 1
end = max(klist)

while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in klist:
        line += i // mid

    if line >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)