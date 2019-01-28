# Uses python3
import sys

def q6_lastdigitFibSum(p_num):

    if p_num == 0:
        return 0

    first = 0
    last = 1
    total = 0

    for _ in range(p_num):

        first, last, total = last, last + first, total + last

    str_total = str(total)

    return str_total[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(q6_lastdigitFibSum(n))

# 100 = 5