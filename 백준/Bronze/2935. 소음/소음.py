import sys
 
a = int(sys.stdin.readline().rstrip())
sig = str(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
 

if sig == '+':
	print(a+b)
if sig == '*':
	print(a*b)