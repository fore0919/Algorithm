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
