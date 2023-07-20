def test_fib(n):
    if n <= 1:
        print(fac(n))
    else:
        print(fac(n - 1) + fac(n - 2))


def fac(n):
    if n <= 1:
        return 1
    else:
        return fac(n - 1) + fac(n - 2)