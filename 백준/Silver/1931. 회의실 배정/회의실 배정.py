import sys

n = int(sys.stdin.readline().rstrip())
room = []
last = 0
count = 0

for _ in range(n):
    room.append(list(map(int, (sys.stdin.readline().rstrip().split()))))


room.sort(key=lambda x: (x[1], x[0]))


for i in room:
    if i[0] >= last:
        count += 1
        last = i[1]

print(count)
