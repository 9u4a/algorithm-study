import sys

result = 0
for _ in range(5):
    n = int(sys.stdin.readline().rstrip())
    result += n
print(result)