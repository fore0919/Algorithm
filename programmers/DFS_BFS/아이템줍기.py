"""
https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1] * 101 for _ in range(101)]
    visit = [[0] * 101 for _ in range(101)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    q.append((characterX * 2, characterY * 2))
    for r in rectangle:
        ax, ay, bx, by = map(lambda x: x * 2, r)
        for i in range(ax, bx + 1):
            for j in range(ay, by + 1):
                if ax < i < bx and ay < j < by:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visit[x][y] // 2
            break
        for dxx, dyy in zip(dx, dy):
            nx, ny = dxx + x, dyy + y
            if 0 < nx < 101 and 0 < ny < 101 and not visit[nx][ny]:
                if graph[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
    return answer
