def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if answers[i] == supo1[i % 5]:
            score[0] += 1
        if answers[i] == supo2[i % 8]:
            score[1] += 1
        if answers[i] == supo3[i % 10]:
            score[2] += 1

    winner = max(score)

    for i in range(3):
        if winner == score[i]:
            answer.append(i + 1)

    return answer

print(solution([4, 5, 3, 4, 2, 2, 3, 1, 5, 2, 1, 3, 4]))
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

########## enumerate 함수를 사용한 풀이 

def solution2(answers):
    supo = [[1, 2, 3, 4, 5], 
            [2, 1, 2, 3, 2, 4, 2, 5], 
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]] 

    score = [0] * len(supo)
    answer = []

    for i in range(len(supo)):
        for j in range(len(answers)):
            n = len(supo[i])
            if answers[j] == supo[i][j%n]:
                score[i] += 1
    
    for idx, max_score in enumerate(score):
        if max_score == max(score):
            answer.append(idx+1)

    return answer

print(solution2([4, 5, 3, 4, 2, 2, 3, 1, 5, 2, 1, 3, 4]))
print(solution2([1, 2, 3, 4, 5]))
print(solution2([1, 3, 2, 4, 2]))