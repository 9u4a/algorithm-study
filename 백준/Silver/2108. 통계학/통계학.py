import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
listn = []
for _ in range(n):
    listn.append(int(sys.stdin.readline().rstrip()))

print(round(sum(listn) / len(listn)))
listn.sort()
print(listn[len(listn) // 2])
c = Counter(listn).most_common(2)
if len(c) > 1 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])
print(listn[-1] - listn[0])