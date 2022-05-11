import sys

a = int(sys.stdin.readline().rstrip())
b = 0
for i in range(1, a+1):
    b += i
print(b)
