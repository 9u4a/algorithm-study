import sys

a = int(sys.stdin.readline().rstrip())
grword = 0
for _ in range(a):
    group_word = sys.stdin.readline().rstrip()
    count = 0
    for x in range(len(group_word) - 1):
        if group_word[x] != group_word[x + 1]:
            word = group_word[x + 1:]
            if word.count(group_word[x]) > 0:
                count += 1
    if count == 0:
        grword += 1
print(grword)