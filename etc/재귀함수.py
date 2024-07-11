# 1 1 2 3 5 8 13 21 34
# 1 2 3 4 5 6 7  8  9


def fibo(n):
    if n < 3:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(5))

####################################


fibo = lambda n: 1 if n <= 2 else fibo(n - 1) + fibo(n - 2)

fibo = lambda n, a=0, b=1: a if n <= 0 else fibo(n - 1, b, a + b)


print(fibo(5))


####################################


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib(3))

####################################


def fib(n):
    a, b = 0, 1
    for i in range(n + 1):
        yield a
        a, b = b, a + b


fib = fib(8)
for i, val in enumerate(fib):
    print("Fibonacci({}): {}".format(i, str(val)))

# 결과
# Fibonacci(0): 0
# Fibonacci(1): 1
# Fibonacci(2): 1
# Fibonacci(3): 2
# Fibonacci(4): 3
# Fibonacci(5): 5
# Fibonacci(6): 8
# Fibonacci(7): 13
# Fibonacci(8): 21

####################################


def factorial(n):
    if n == 1:  # n이 1일 때
        return 1  # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(
        n - 1
    )  # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함


print(factorial(5))

####################################


def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_iterative(5))
