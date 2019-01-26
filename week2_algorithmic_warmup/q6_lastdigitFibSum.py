# Uses python3
import sys
from collections import deque

def q6_lastdigitFibSum(p_num):

    if p_num == 0:
        return 0

    total = 1
    fib_lst = deque([0, 1])

    for i in range(1, p_num):

        fib_lst.append(fib_lst[-1] + fib_lst[-2])
        total = total + fib_lst[-1]
        fib_lst.popleft()
    str_total = str(total)

    return str_total[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(q6_lastdigitFibSum(n))

