
def fib_efficient(n, p_period, p_mod):
    """
    >>> fib_efficient(2015, 8, 3)
    1

    >>> fib_efficient(1000, 60, 10)
    5

    :return:
    """
    mod = n % p_period
    last_fib = mod % p_mod

    return last_fib

