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


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12971
"""


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp = [0 for _ in range(len(sticker))]
    dp[0] = sticker[0]
    dp[1] = sticker[0]

    dp2 = [0 for _ in range(len(sticker))]
    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    value_1 = max(dp)

    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    value_2 = max(dp2)

    answer = max(value_1, value_2)
    return answer


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12979#
"""


def solution(n, stations, w):
    answer = 0
    r = w * 2 + 1
    start = 1
    end = 0
    for station in stations:
        end = station - w - start
        if not (station - w) <= start:
            answer += (end) // r if (end) % r == 0 else (end) // r + 1
        start = station + w + 1
    if start <= n:
        end = (n + 1) - start
        answer += (end) // r if (end) % r == 0 else (end) // r + 1
    return answer
