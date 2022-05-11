import sys

a, b = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
for i in x:
    if i < b:
        print(i, end=" ")
