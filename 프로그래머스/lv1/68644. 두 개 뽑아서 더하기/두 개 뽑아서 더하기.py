def solution(numbers):
    answer = set()
    for x in range(len(numbers)):
        for y in range(x+1, len(numbers)):
            answer.add(numbers[x]+numbers[y])
    result = list(answer)
    result.sort()
    return result