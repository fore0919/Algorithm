"""
https://school.programmers.co.kr/learn/courses/30/lessons/12927
"""


# 효율성 통과 실패
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    while n:
        works[works.index(max(works))] -= 1
        n -= 1
    return sum([work * work for work in works])


# 효율성 통과 성공
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)
    for i in range(n):
        m = max(works)
        j = 0
        while 1:
            if works[j] != m:
                break
            works[j] -= 1
            n -= 1
            j += 1
            if n == 0:
                break
        if n == 0:
            break
    for work in works:
        answer += work * work
    return answer


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12938#
"""
import math


def solution(n, s):
    answer = []
    cnt = s % n
    if s < n:
        return [-1]
    while len(answer) != n:
        if cnt > 0:
            cnt -= 1
            answer.append(math.ceil(s / n))
        else:
            answer.append(s // n)
    return sorted(answer)
