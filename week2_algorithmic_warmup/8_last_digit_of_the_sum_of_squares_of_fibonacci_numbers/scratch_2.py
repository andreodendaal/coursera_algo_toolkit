



def fib_efficient(n, p_period,  p_mod):
    """
    >>> fib_efficient(2015, 8, 3)
    1

    :return:
    """
    mod = n % p_period
    last_fib = mod % p_mod

    return last_fib

def get_pisano(modulo):

    previous = 1
    current = 1

    result = 1
    while not (previous == 0 and current == 1):  # 1
        buffer = (previous + current) % modulo  # 2
        previous = current
        current = buffer

        result += 1

    return result


print(5 % 60)