import sys

n, m = map(int, sys.stdin.readline().split())
listx = list(map(int, sys.stdin.readline().split()))


def solve(N, M, xlist):
    count = 0
    result = 0
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                result = xlist[i] + xlist[j] + xlist[k]
                if result <= M:
                    count = (result if count < result else count)
                if count == M:
                    return count
    return count


print(solve(n, m, listx))
