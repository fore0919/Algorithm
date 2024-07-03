"""
https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0

    while len(truck_weights) > 0:
        answer += 1
        current_weight = current_weight - bridge.popleft()
        if truck_weights[0] + current_weight <= weight:
            current_weight = current_weight + truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    answer += bridge_length
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
result = 8
bridge_length = 100
weight = 100
truck_weights = [10]
result = 101
bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
result = 110
