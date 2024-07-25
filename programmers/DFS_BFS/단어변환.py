"""
https://school.programmers.co.kr/learn/courses/30/lessons/43163#
"""

from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    q = deque()
    q.append([begin, 0])

    while q:
        current, cnt = q.popleft()

        if current == target:
            answer = cnt
            break

        for word in words:
            count = 0
            for i in range(len(current)):
                if current[i] != word[i]:
                    count += 1

            if count == 1:
                q.append([word, cnt + 1])
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# return : 4

print(solution(begin, target, words))
