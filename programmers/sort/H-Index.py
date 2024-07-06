"""
https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""


def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


citations = [3, 0, 6, 1, 5]
# result : 3
