from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices) > 0:
        seconds = 0
        price = prices.popleft()
        for p in prices:
            seconds += 1
            if price > p:
                break
        answer.append(seconds)
    return answer


prices = [1, 2, 3, 2, 3]
# result : [4, 3, 1, 1, 0]
