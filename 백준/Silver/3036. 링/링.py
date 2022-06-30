import sys
import fractions

n = int(sys.stdin.readline().rstrip())
r = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    result = fractions.Fraction(r[0], r[i])
    print("{}/{}".format(result.numerator, result.denominator))
