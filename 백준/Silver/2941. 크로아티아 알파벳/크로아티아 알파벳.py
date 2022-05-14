import sys

a = sys.stdin.readline().rstrip()
count = 0
alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alp:
    a = a.replace(i, '@')
print(len(a))
