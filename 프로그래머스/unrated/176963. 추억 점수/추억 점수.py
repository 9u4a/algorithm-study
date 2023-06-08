def solution(name, yearning, photo):
    answer = []
    match = dict()
    
    for i in range(len(name)):
        match[name[i]] = yearning[i]
        
    for p1 in photo:
        total = 0
        for p2 in p1:
            if p2 in match:
                total += match[p2]
        answer.append(total)
        
    return answer