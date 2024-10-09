"""
https://school.programmers.co.kr/learn/courses/30/lessons/340198#
테스트 케이스 통과 실패 -> 반례 부족
"""


def solution(mats, park):
    answer = -1
    flag = "-1" or "1"
    for i in range(len(park)):
        for j in range(len(park[i])):
            if (j + 1 == len(park[i])) or (i + 1 == len(park)):
                park[i][j] = "1"
                break
            else:
                if (
                    park[i][j] == flag
                    and park[i + 1][j] == flag
                    and park[i][j + 1] == flag
                    and park[i + 1][j + 1] == flag
                ):
                    (
                        park[i][j],
                        park[i + 1][j],
                        park[i][j + 1],
                        park[i + 1][j + 1],
                    ) = ("1", "1", "1", "1")
    empty = int(sum(park, []).count("1") ** 0.5)
    mat = list(filter(lambda x: x <= empty, mats))
    if mat:
        answer = max(mat)
    return answer
