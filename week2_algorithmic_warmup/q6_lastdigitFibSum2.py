# Uses python3
import sys
from collections import deque

def q6_lastdigitFibSum(p_num):

    if p_num == 0:
        return 0

    values = [0, 1]

    for i in range(p_num + 1):

        values.append((values[0] + values[1]) % 3)
        if values[-2:] == [0, 1]:
            mod_value = i

        #values[0], values[1] = values[1], values[1] + values[0]
    str_total = str(values[-1] - 1)
    return str_total[-1], values


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(q6_lastdigitFibSum(n))

# 100 = 5
# sum of 100  = 927372692193078999175.
# 101th value = 927372692193078999176
# 100 th value = 573147844013817084101
# sum of 50 =    32951280098
# 51 th value =  32951280099