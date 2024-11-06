"""
Bracket Combinations
Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, 
and return the number of valid combinations that can be formed with num pairs of parentheses. 
For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis,
namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). 
There are 5 total combinations when the input is 3, so your program should return 5.
"""

# 카탈란 수 알고리즘
# 점화식: Catalan(n) = 2n! / (n! * (n+1)!)

import math


def BracketCombinations(num):
    def func(n):
        if n == 1:
            return 1
        return n * func(n - 1)

    return int(func(2 * num) / (func(num + 1) * func(num)))


# 한줄 풀이
def BracketCombinations2(num):
    return math.factorial(2 * num) // (
        math.factorial(num) * math.factorial(num + 1)
    )


print(BracketCombinations(3))  # result : 5
print(BracketCombinations2(3))  # result : 5
