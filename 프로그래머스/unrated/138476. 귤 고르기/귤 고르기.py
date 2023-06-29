from collections import Counter
def solution(k, tangerine):
    answer = 0
    tan = Counter(tangerine)
    
    for i in sorted(tan.values(), reverse = True):
        k -= i
        answer +=1
        if k <= 0:
            break
    return answer