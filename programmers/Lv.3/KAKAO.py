"""
https://school.programmers.co.kr/learn/courses/30/lessons/64064
"""


def solution(user_id, banned_id):
    answer = []
    result = [[]]
    for banned in banned_id:
        idx = []
        _list = []
        for i, j in enumerate(banned):
            if j == "*":
                idx.append(i)

        for user in user_id:
            user_name = list(user)
            if len(user) == len(banned):
                for k in idx:
                    user_name[k] = "*"

            user_name = "".join(user_name)
            if user_name == banned:
                for r in result:
                    if user not in r:
                        _list.append(r + [user])
        result = _list

    for name in result:
        if set(name) not in answer:
            answer.append(set(name))

    return len(answer)


"""
https://school.programmers.co.kr/learn/courses/30/lessons/67258
"""

from collections import defaultdict


def solution(gems):
    min_gems = int(1e9)
    len_gems = len(gems)
    n_gems = len(set(gems))
    end = 0
    temp = defaultdict(lambda: 0)
    for start, gem in enumerate(gems):
        while len(temp) < n_gems and end < len_gems:
            temp[gems[end]] += 1
            end += 1
        if len(temp) == n_gems:
            if min_gems > end - start:
                min_gems = end - start
                result = [start + 1, end]
        temp[gem] -= 1
        if temp[gem] == 0:
            del temp[gem]
    return result


"""
https://school.programmers.co.kr/learn/courses/30/lessons/64062
"""


# 효율성 통과 X
def solution(stones, k):
    windows = max(stones[:k])
    for i in range(k, len(stones) - k + 1):
        num = max(stones[i : k + i])
        windows = min(windows, num)
    return windows


# 효율성 통과 O
from collections import deque


def solution(stones, k):
    stones = list(zip(range(1, len(stones) + 1), stones))
    q = deque()
    answer = float("inf")
    for idx, val in stones:
        while q:
            if q[0][0] <= (idx - k):
                q.popleft()
            elif q[-1][1] < val:
                q.pop()
            else:
                break
        q.append((idx, val))
        if idx >= k:
            answer = min(q[0][1], answer)
    return answer
