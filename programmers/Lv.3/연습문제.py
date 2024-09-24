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


"""
https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3
"""

from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [-1] * (n + 1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque([1])
    distance[1] = 0

    while q:
        current = q.popleft()
        for i in graph[current]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[current] + 1

    return distance.count(max(distance))
