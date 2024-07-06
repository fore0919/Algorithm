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
    numbers = list(numbers)
    combination = set(map("".join, permutations(numbers)))
    _list = list(combination) + numbers
    int_list = list(set(map(lambda x: int(x), _list)))

    for num in int_list:
        if is_prime(num):
            result.append(num)

    return len(set(result))

    temp = []
    for i in range(1, len(numbers) + 1):
        temp += list(permutations(numbers, i))

    answer = [int("".join(i)) for i in temp]
    answer = [i for i in set(answer) if is_prime(i) == True]
    return len(answer)
