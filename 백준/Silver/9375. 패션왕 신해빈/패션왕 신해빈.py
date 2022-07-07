import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    clothes_dict = {}
    result = 1
    for _ in range(n):
        name, clothes = map(str, sys.stdin.readline().split())
        if clothes in clothes_dict:
            clothes_dict[clothes] += 1
        else:
            clothes_dict[clothes] = 1
    for c in clothes_dict:
        result *= clothes_dict[c] + 1
    result -= 1
    print(result)
