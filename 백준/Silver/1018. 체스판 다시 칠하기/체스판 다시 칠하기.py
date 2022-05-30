import sys

n, m = map(int, sys.stdin.readline().split())
chessboard = []
for _ in range(n):
    chessboard.append(sys.stdin.readline().rstrip())


def solve(listx, x, y):
    count = []
    for a in range(x - 7):
        for b in range(y - 7):
            white = black = 0
            for i in range(a, a + 8):
                for j in range(b, b + 8):
                    if (i + j) % 2 == 0:
                        if listx[i][j] == 'W':
                            white += 1
                        else:
                            black += 1
                    else:
                        if listx[i][j] == 'B':
                            white += 1
                        else:
                            black += 1
            count.append(min(white, black))
    return min(count)


print(solve(chessboard, n, m))
