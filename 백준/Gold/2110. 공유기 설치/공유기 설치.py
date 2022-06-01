import sys

n, c = map(int, sys.stdin.readline().split())
home = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
home.sort()
start = 1
end = home[-1] - home[0]
solve = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    line = home[0]
    for i in range(1, n):
        if home[i] >= line + mid:
            count += 1
            line = home[i]

    if count >= c:
        start = mid + 1
        solve = mid
    else:
        end = mid - 1

print(solve)
