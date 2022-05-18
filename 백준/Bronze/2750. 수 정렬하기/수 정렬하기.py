import sys

n = int(sys.stdin.readline().rstrip())
listn = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
listn.sort()
print(*listn, sep='\n')