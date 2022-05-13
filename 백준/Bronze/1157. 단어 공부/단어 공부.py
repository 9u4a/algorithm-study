import sys

s = sys.stdin.readline().rstrip().upper()
wordlist = list(set(s))
countlist = []
for y in wordlist:
    countlist.append(s.count(y))

if countlist.count(max(countlist)) > 1:
    print('?')
else:
    max_index = countlist.index(max(countlist))
    print(wordlist[max_index])