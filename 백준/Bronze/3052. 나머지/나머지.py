import sys

x = []

for i in range(10):
    a = (int(sys.stdin.readline().rstrip())) % 42
    if a not in x:
        x.append(a)

print(len(x))
