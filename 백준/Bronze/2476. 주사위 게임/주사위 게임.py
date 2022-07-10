import sys

n = int(sys.stdin.readline().rstrip())
result = []
for _ in range(n):
	dice = list(map(int, sys.stdin.readline().split()))
	if dice[0] == dice[1] and dice[1] == dice[2]:
		result.append(10000 + dice[0] * 1000)
	elif dice[0]== dice[1]:
		result.append(1000 + dice[0] * 100)
	elif dice[1] == dice[2]:
		result.append(1000 + dice[1] * 100)
	elif dice[0] == dice[2]:
		result.append(1000 + dice[2] * 100)
	else:
		result.append(max(dice) * 100)

print(max(result))