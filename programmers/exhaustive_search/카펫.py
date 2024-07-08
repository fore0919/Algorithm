"""
https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""


def solution(brown, yellow):
    answer = []
    w = 0
    h = 0
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = yellow // i
            h = i
            if w * 2 + h * 2 + 4 == brown:
                answer.append(w + 2)
                answer.append(h + 2)
                break
    answer.sort(reverse=True)
    return answer


brown = 10
yellow = 2  # return [4, 3]
print(solution(brown, yellow))


import math


def solution(brown, yellow):
    answer = []

    s = brown + yellow
    b = (brown + 4) / 2  # == w+h (가로+세로)
    answer.append(int((b + math.sqrt(b**2 - 4 * s)) / 2))
    answer.append(int((b - math.sqrt(b**2 - 4 * s)) / 2))
    return answer


"""
갈색 블럭 갯수 : brown = 2w + (h-2) * 2 -> 2w + 2h - 4 (모서리 겹치는 부분)
1. 가로 세로 합 : w + h = (brown + 4) / 2 
2. 넓이 : w * h = s (brown + yellow)

1. h = (brown + 4) / 2 - w
2. w * ((brown + 4) / 2 - w) = s 
    -> w(brown + 4) / 2 - w^2 = s 
    -> w(brown + 4) / 2 - w^2 - s = 0 

이차 방정식 형태로 변환 : ax^2 + bx + c = 0 
3. - w^2 + ((brown + 4) / 2)w - s = 0 
    -> w^2 - ((brown + 4) / 2)w + s = 0 (양수로 변환)

근의 공식 적용 
4.  w = -b +- sqrt(b^2 - 4ac) / 2a
대입 : a = 1, b = -(b+4)/2, c = s 
"""
