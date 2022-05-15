import sys

x = int(sys.stdin.readline().rstrip())
line = 0
end = 0
while x > end:
    line += 1
    end += line

num = end - x
if line % 2 == 0:
    a = line - num
    b = num + 1
else:
    a = num + 1
    b = line - num

print(a, "/", b, sep="")