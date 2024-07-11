"""
https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""

import string


def solution(name):
    answer = 0
    upper = list(enumerate([i for i in string.ascii_uppercase]))
    reverse = list(enumerate(reversed([i for i in string.ascii_uppercase])))
    length = len(name)
    min_move = length - 1

    for i in range(length):
        idx = i + 1
        while (idx < length) and (name[idx] == "A"):
            idx += 1

        right = length - idx
        back = min(i, right)
        min_move = min(min_move, i + right + back)

        move = [0, 0]
        for u in upper:
            if name[i] == u[1]:
                move[0] = u[0]
        for r in reverse:
            if name[i] == r[1]:
                move[1] = r[0] + 1

        answer += min(move)
    answer += min_move
    return answer


name = "JEROEN"
# return: 56
name = "JAN"
# return:23
print(solution(name))
