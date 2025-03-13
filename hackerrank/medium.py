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
