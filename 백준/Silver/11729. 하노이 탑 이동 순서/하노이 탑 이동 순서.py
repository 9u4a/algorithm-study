import sys


def solve(x, from_, to_, by_):
    if x == 1:
        print(from_, to_)
        return

    solve(x - 1, from_, by_, to_)
    print(from_, to_)
    solve(x - 1, by_, to_, from_)


n = int(sys.stdin.readline().rstrip())
print(2 ** n - 1)
solve(n, 1, 3, 2)