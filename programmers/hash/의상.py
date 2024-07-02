"""
https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""


def solution(clothes):
    answer = 0
    hash_map = {}
    for value, key in clothes:
        hash_map[key] = hash_map.get(key, 0) + 1
    # closet = {'headgear': 2, 'eyewear': 1}

    # 경우의 수 구하기 A의 종류가 N개, B의 종류가 M개 일 때 (N+1)(M+1)
    answer = 1
    for h in hash_map:
        answer *= hash_map[h] + 1
    return answer - 1


clothes1 = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]  # result : 5
clothes2 = [
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"],
]  # result : 3


"""
(N+1)(M+1) = NM + N + M + 1

NM: N과 M을 모두 사용하는 경우
N: N만 사용하는 경우
M: M만 사용하는 경우
1: 모두 사용하지 않는 경우 
 
(N+1)(M+1)에는 A, B 모두를 사용하지 않는 경우가 포함
해당 문제에선 아무것도 입지않는 경우를 제외해야 하기 때문에 - 1
"""
