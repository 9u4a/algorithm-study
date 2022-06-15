import sys

n = sys.stdin.readline().rstrip()
result = ''
for i in n:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()
print(result)
