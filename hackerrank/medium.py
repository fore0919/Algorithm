"""
Example
The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
"""

if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append((name, score))
    arr.sort(key=lambda x: (x[1], x[0]))
    score = list(set(sorted(j for i, j in arr)))[1]
    for i, j in arr:
        if j == score:
            print(i)

"""
Find Angle MBC
"""
import cmath
import math

ab = int(input())
bc = int(input())

# solution 1
# math.atan() -> 역탄젠트 함수 (라디안 값 반환)
# math.degrees() -> 라디안 값을 도(degree) 단위로 변환
theta = round(math.degrees(math.atan(ab / bc)))
print(f"{theta}\u00b0")  # \u00B0 -> 유니코드 문자(°, degree symbol) 각도 기호

# solution 2
ac = math.sqrt(ab**2 + bc**2)  # 빗변
mc = ac / 2  # 중점
result = (ac**2 + bc**2 - ab**2) / (2 * bc * ac)  # 코사인 법칙
angleC = cmath.acos(result)  # cmath.acos() -> 역코사인 함수 (라디안 값 반환)

# 중점에서 높이 계산
md = mc * (cmath.sin(angleC))
db = bc - (mc * (cmath.cos(angleC)))

# 복소수로 벡터를 표현하여 각도 구하기
r = complex(db, md)
angle = round(math.degrees(cmath.phase(r).real))
a = str(angle) + chr(176)
print(a)


def solution(diamond_n, diamond):
    diamond = [[3], [4, 1], [7, 9, 2], [2, 7, 9, 6], [1, 9, 5], [7, 3], [9]]
    diamond_n = 4
    n = len(diamond)
    mid = len(diamond) // 2

    dp_up = [[0] * len(row) for row in diamond]
    dp_down = [[0] * len(row) for row in diamond]

    dp_up[0][0] = diamond[0][0]
    for i in range(1, mid + 1):
        for j in range(len(diamond[i])):
            if j == 0:
                dp_up[i][j] = dp_up[i - 1][j] + diamond[i][j]
            elif j == len(diamond[i]) - 1:
                dp_up[i][j] = dp_up[i - 1][j - 1] + diamond[i][j]
            else:
                dp_up[i][j] = (
                    max(dp_up[i - 1][j - 1], dp_up[i - 1][j]) + diamond[i][j]
                )

    dp_down[-1][0] = diamond[-1][0]
    for i in range(n - 2, mid - 1, -1):
        for j in range(len(diamond[i])):
            if j == 0:
                dp_down[i][j] = dp_down[i + 1][j] + diamond[i][j]
            elif j < len(diamond[i + 1]):
                dp_down[i][j] = (
                    max(dp_down[i + 1][j], dp_down[i + 1][j - 1])
                    + diamond[i][j]
                )
            else:
                dp_down[i][j] = dp_down[i + 1][j - 1] + diamond[i][j]

    return max(dp_up[mid]) + max(dp_down[mid + 1])
    max_sum = 0
    for j in range(len(diamond[mid])):
        if j < len(dp_up[mid]) and j < len(dp_down[mid]):
            max_sum = max(
                max_sum, dp_up[mid][j] + dp_down[mid][j] - diamond[mid][j]
            )
    return max_sum


def solution2(diamond_n, diamond):
    diamond = [[3], [4, 1], [7, 9, 2], [2, 7, 9, 6], [1, 9, 5], [7, 3], [9]]
    diamond_n = 4
    n = len(diamond)
    dp = [[0] * len(row) for row in diamond]
    dp[0][0] = diamond[0][0]

    for i in range(1, n):
        for j in range(len(diamond[i])):
            _max = 0
            if len(diamond[i]) > len(diamond[i - 1]):
                if j - 1 >= 0:
                    _max = max(_max, dp[i - 1][j - 1])
                if j < len(dp[i - 1]):
                    _max = max(_max, dp[i - 1][j])
            else:
                if j < len(dp[i - 1]):
                    _max = max(_max, dp[i - 1][j])
                if j + 1 < len(dp[i - 1]):
                    _max = max(_max, dp[i - 1][j + 1])
            dp[i][j] = _max + diamond[i][j]
    return dp[-1]
