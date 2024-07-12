"""
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""

from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for dungeon in permutations(dungeons, len(dungeons)):
        temp = k
        cnt = 0
        for d in dungeon:
            if d[0] <= temp:
                temp -= d[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
# result: 3
