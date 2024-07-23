"""
https://school.programmers.co.kr/learn/courses/30/lessons/42898
"""


def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]
    dp = [[0] * (m + 1) for i in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            # 현재 칸 까지의 이동 경로 수는 (왼쪽칸까지의 이동경로수 -1) + (윗쪽칸까지의 이동경로수 -1 )이다
    return dp[n][m]


m = 4
n = 3
puddles = [[2, 2]]
# return : 4
print(solution(m, n, puddles))
