"""
https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""


def solution(priorities, location):
    answer = 0
    queue = [queue for queue in enumerate(priorities)]
    while True:
        q = queue.pop(0)
        if any(q[1] < v[1] for v in queue):
            queue.append(q)
        else:
            answer += 1
            if q[0] == location:
                return answer
    return answer


priorities = [2, 1, 3, 2]
location = 2
# result : 1
priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0
# result :5
