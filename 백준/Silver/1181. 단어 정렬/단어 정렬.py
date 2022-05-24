import sys

n = int(sys.stdin.readline().rstrip())
sortList = []
for i in range(n):
    sortList.append(sys.stdin.readline().rstrip())

sortList = list(set(sortList))
sortList.sort()
sortList.sort(key=len)

for i in sortList:
    print(i)
