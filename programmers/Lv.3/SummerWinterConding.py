"""
https://school.programmers.co.kr/learn/courses/30/lessons/12987#
"""

from collections import deque


def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    q = deque(B)
    for a in A:
        if a < q[0]:
            answer += 1
            q.popleft()
    return answer
