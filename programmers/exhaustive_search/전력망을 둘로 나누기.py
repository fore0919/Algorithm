"""
https://school.programmers.co.kr/learn/courses/30/lessons/86971#
"""

"""
테스트 실패 케이스 : 간선을 가장 많이 갖고있는 노드 사이를 끊는 방법

wires = [[2, 1], [3, 1], [1, 4], [4, 5], [5, 6], [7, 6], [8, 6]]
n = 8
result = 0

해당 케이스의 경우 실패한다.
"""
import statistics
from collections import Counter


def failed_solution(n, wires):
    answer = []
    array = sum(wires, [])
    counter = {k: v for k, v in dict(Counter(array)).items() if v == 1}
    max_arr = []
    min_arr = list(counter.keys())
    _max = statistics.mode(array)

    for i in range(len(wires)):
        if _max in wires[i]:
            if not (wires[i][0] and wires[i][1] in min_arr):
                max_arr.append(i)

    for m in max_arr:
        cnt = len(wires[:m]) - len(wires[m + 1 :])
        answer.append(abs(cnt))
    return min(answer)


"""
BFS(너비 우선 탐색)를 이용한 방식
"""

from collections import deque


def bfs(graph, i, visit, connect):
    queue = deque([i])
    visit[i] = True
    cnt = 1
    while queue:
        q = queue.popleft()
        for g in graph[q]:
            if not visit[g] and connect[i][g]:
                queue.append(g)
                visit[g] = True
                cnt += 1
    return cnt


"""
DFS(깊이 우선 탐색)를 이용한 방식
"""


def dfs(graph, i, visit, connect):
    cnt = 1
    visit[i] = True
    for v in graph[i]:
        if not visit[v] and connect[i][v]:
            cnt += dfs(graph, v, visit, connect)
    return cnt


"""
그래프를 돌면서 전력망을 하나씩 끊는 방식
전력망 끊기 -> dfs/bfs로 양쪽 네트워크의 수를 구한 후 해당 값의 차이 -> 전력망 연결
끊은 간선의 양끝부터 시작해서 도착했을때 송전탑의 갯수를 구하는 방법.


DFS(깊이우선탐색): 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색 | 스택, 재귀함수 | 경로의 특징 
BFS(너비우선탐색): 현재 정점에 연결된 가까운 점들부터 탐색 | 큐 | 최단거리

"""


def solution(n, wires):
    answer = float("inf")
    connect = [[True] * (n + 1) for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)

    for start, end in wires:
        visit = [False] * (n + 1)
        connect[start][end] = False
        count_s = dfs(graph, start, visit, connect)
        count_e = dfs(graph, end, visit, connect)
        # count_s = bfs(graph, start, visit, connect)
        # count_e = bfs(graph, end, visit, connect)
        connect[start][end] = True
        answer = min(answer, abs(count_s - count_e))
    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
# result : 3
n = 4
wires = [[1, 2], [2, 3], [3, 4]]
# result :0
n = 7
wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
# result :1

print(solution(n, wires))
