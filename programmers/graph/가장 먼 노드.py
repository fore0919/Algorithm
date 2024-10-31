"""
https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""

from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [-1] * (n + 1)
    distance[1] = 0
    q = deque([1])

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    while q:
        current = q.popleft()
        for i in graph[current]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[current] + 1

    return distance.count(max(distance))
