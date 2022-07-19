import sys

n = int(sys.stdin.readline().rstrip())
a = 100
b = 100
for _ in range(n):
    ascore,bscore = map(int, sys.stdin.readline().split())

    if ascore > bscore:
        b -= ascore
    elif bscore > ascore:
        a -= bscore
print(a)
print(b)
