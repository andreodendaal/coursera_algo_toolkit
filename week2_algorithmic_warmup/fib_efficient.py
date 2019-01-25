# Uses python3
def fib_efficient(n):
    """

    >>> fib_efficient(1000)
    5

    >>> fib_efficient(3)
    2

    >>> fib_efficient(239)
    1


    :return:
    """
    if n <= 1:
        return n

    values = [0, 1]
    for i in range(2,  (n + 1)):
        values.append((values[i - 1] + values[i - 2]) % 10)

    return values[i]


