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


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12926
"""


def solution(s, n):
    answer = ""
    for string in s:
        if string.isalpha():
            if string.upper() == string:
                end = ord("Z")
            else:
                end = ord("z")
            i = ord(string) + n
            answer += chr(i if i <= end else i - 26)
        else:
            answer += string
    return answer


"""
https://school.programmers.co.kr/learn/courses/30/lessons/178871
"""


def solution(players, callings):
    hash_map = dict(zip(players, range(len(players))))
    for name in callings:
        current_idx = hash_map[name]
        pass_idx = current_idx - 1
        players[current_idx], players[pass_idx] = (
            players[pass_idx],
            players[current_idx],
        )
        hash_map[name] = pass_idx
        hash_map[players[current_idx]] = current_idx
    return players
