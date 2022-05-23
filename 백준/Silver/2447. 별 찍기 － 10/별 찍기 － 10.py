import sys


def solve(x):
    if x == 3:
        starlist[0][:3] = starlist[2][:3] = ['*'] * 3
        starlist[1] = ['*', ' ', '*']
        return
    y = x // 3
    solve(y)

    for a in range(0, x, y):
        for b in range(0, x, y):
            if a != y or b != y:
                for c in range(y):
                    starlist[a + c][b:b + y] = starlist[c][:y]


n = int(sys.stdin.readline().rstrip())
starlist = [[' ' for _ in range(n)] for _ in range(n)]

solve(n)

for i in range(n):
    for j in range(n):
        print(starlist[i][j], end='')
    print()
