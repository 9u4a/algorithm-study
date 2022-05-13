import sys

a = int(sys.stdin.readline().rstrip())

for _ in range(a):
    x = list(map(float, sys.stdin.readline().split()))
    total = 0
    count = x[0]
    count2 = 0.0
    for i in range(1, len(x)):
        total += x[i]

    avg = total/count
    for y in x[1:]:
        if y > avg:
            count2 += 1

    print("{:.3f}%".format(count2/count*100))
