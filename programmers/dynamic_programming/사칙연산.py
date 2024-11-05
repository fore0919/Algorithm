"""
https://school.programmers.co.kr/learn/courses/30/lessons/1843
"""


def solution(arr):
    num = len(arr) // 2 + 1
    dp_min = [
        [10000 if i != j else int(arr[i * 2]) for i in range(num)]
        for j in range(num)
    ]
    dp_max = [
        [-10000 if i != j else int(arr[i * 2]) for i in range(num)]
        for j in range(num)
    ]
    for n in range(1, num):
        for i in range(num - n):
            j = i + n
            for k in range(i, j):
                if arr[2 * k + 1] == "+":
                    dp_max[i][j] = max(
                        dp_max[i][k] + dp_max[k + 1][j], dp_max[i][j]
                    )
                    dp_min[i][j] = min(
                        dp_min[i][k] + dp_min[k + 1][j], dp_min[i][j]
                    )
                else:
                    dp_max[i][j] = max(
                        dp_max[i][k] - dp_min[k + 1][j], dp_max[i][j]
                    )
                    dp_min[i][j] = min(
                        dp_min[i][k] - dp_max[k + 1][j], dp_min[i][j]
                    )
    return dp_max[0][num - 1]
