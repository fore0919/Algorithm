"""
https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""

from heapq import heappop, heappush


def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        string, number = operation.split(" ")
        number = int(number)
        if string == "I":
            heappush(heap, number)
        else:
            if heap:
                if number == -1:
                    heappop(heap)
                else:
                    heap.sort()
                    heap.pop()
    heap.sort()
    if heap:
        answer = [heap[-1], heap[0]]
    else:
        answer = [0, 0]

    return answer


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# return : [0,0]
operations = [
    "I -45",
    "I 653",
    "D 1",
    "I -642",
    "I 45",
    "I 97",
    "D 1",
    "D -1",
    "I 333",
]
# return : [333, -45]
print(solution(operations))
