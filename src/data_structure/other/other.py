def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fast_fib(n):
    if n < 3:
        return 1
    first = 1
    second = 1
    for i in range(3, n+1):
        sum = first + second
        first = second
        second = sum

    return second
