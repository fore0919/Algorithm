"""
https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""

import math
from itertools import permutations


def solution(numbers):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for i in range(1, len(numbers) + 1):
        result += list(permutations(numbers, i))

    result = [int("".join(i)) for i in result]
    answer = [num for num in set(result) if is_prime(num)]

    return len(answer)


numbers = "17"  # return : 3
numbers = "011"  # return : 2
print(solution(numbers))
