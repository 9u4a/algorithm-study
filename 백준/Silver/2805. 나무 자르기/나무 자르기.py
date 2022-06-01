import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(tree)
result = 0

while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in tree:
        if (i - mid) >= 0:
            count += i - mid

    if count >= m:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)