"""
https://school.programmers.co.kr/learn/courses/30/lessons/12981
"""


def solution(n, words):
    word = []
    for i in range(1, len(words)):
        word.append(words[i - 1])
        string = word[-1][-1]
        if not words[i].startswith(string) or words[i] in word:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]


n = 3
words = [
    "tank",
    "kick",
    "know",
    "wheel",
    "land",
    "dream",
    "mother",
    "robot",
    "tank",
]
# result : [3,3]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""


def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        skills = list(st)
        cnt = 0
        idx = 0
        while len(st) > cnt:
            current = skills[0]
            if idx >= len(skill) or current not in skill:
                skills.pop(0)
            elif current == skill[idx]:
                skills.pop(0)
                idx += 1
            cnt += 1
        if not skills:
            answer += 1
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# result = 2

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12980
"""


def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ans += 1
    return ans


n = 5000  # result : 5

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12978
"""

import heapq


def solution(N, road, K):
    def dijkstra(distance, temp):
        heap = []
        heapq.heappush(heap, [0, 1])
        while heap:
            cost, node = heapq.heappop(heap)
            for c, n in temp[node]:
                if cost + c < distance[n]:
                    distance[n] = cost + c
                    heapq.heappush(heap, [cost + c, n])

    distance = [float("inf")] * (N + 1)
    distance[1] = 0
    temp = [[] for _ in range(N + 1)]
    for r in road:
        temp[r[0]].append([r[2], r[1]])
        temp[r[1]].append([r[2], r[0]])

    dijkstra(distance, temp)
    return len([i for i in distance if i <= K])


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
# result : 4
"""
https://school.programmers.co.kr/learn/courses/30/lessons/49994#
"""


def solution(dirs):
    answer = []
    x, y = 0, 0
    dic = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    for d in dirs:
        start = (x, y)
        if abs(x + dic[d][0]) <= 5 and abs(y + dic[d][1]) <= 5:
            x += dic[d][0]
            y += dic[d][1]
            if answer and ((x, y), start) in answer:
                continue
            answer.append((start, (x, y)))
    return len(set(answer))


"""
https://school.programmers.co.kr/learn/courses/30/lessons/62048
"""

import math


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))
