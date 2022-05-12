import sys

a = int(sys.stdin.readline().rstrip())
x = list(map(float, sys.stdin.readline().split()))
total = 0.0
for b in x:
    total += b
print(total/len(x)/max(x)*100)
