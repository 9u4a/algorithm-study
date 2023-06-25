def solution(sequence, k):
    answerLen = k
    rpointer = 0
    sequenceSum = 0
    sequenceLen = len(sequence)
    answer = []
    
    for lpointer in range(sequenceLen):
        
        while sequenceSum < k and rpointer < sequenceLen:
            sequenceSum += sequence[rpointer]
            rpointer += 1
        
        if sequenceSum == k and (rpointer - 1 - lpointer) < answerLen:
            answer = [lpointer, rpointer - 1]
            answerLen = rpointer - 1 - lpointer
            
        sequenceSum -= sequence[lpointer]
        
    return answer
            