import sys

v = int(sys.stdin.readline().rstrip())
total = sys.stdin.readline().rstrip()

a = total.count('A')
b = total.count('B')

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
