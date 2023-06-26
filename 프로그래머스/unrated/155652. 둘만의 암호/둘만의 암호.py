def solution(s, skip, index):
    abclist = [chr(i) for i in range(ord('a'), ord('z') + 1) if not chr(i) in skip] * 3
    result = ""
    for i in s:
        result += abclist[abclist.index(i) + index]
    return result