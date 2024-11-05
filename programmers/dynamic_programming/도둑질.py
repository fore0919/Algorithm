"""
https://school.programmers.co.kr/learn/courses/30/lessons/42897
"""


def solution(money):
    dp_first = [0] * len(money)
    dp_first[0] = money[0]
    dp_first[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp_first[i] = max(dp_first[i - 1], money[i] + dp_first[i - 2])
    dp_last = [0] * len(money)
    dp_last[0] = 0
    dp_last[1] = money[1]
    for i in range(2, len(money)):
        dp_last[i] = max(dp_last[i - 1], money[i] + dp_last[i - 2])
    return max(max(dp_first), max(dp_last))
