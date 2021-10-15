m = {}


def fibonacci(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    elif n in m:
        return m[n]
    else:
        f = fibonacci(n - 1) + fibonacci(n - 2)
        m[n] = f
        return f


def fibonacci_max(x):
    n = 0
    while True:
        f = fibonacci(n)
        if f > x:
            break
        n += 1
    return fibonacci(n - 1)
