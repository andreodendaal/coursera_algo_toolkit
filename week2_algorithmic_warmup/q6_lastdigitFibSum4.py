# Uses python3
import sys


def q6_lastdigitFibSum(p_num):

    if p_num == 0:
        return 0

    values = [0, 1]

    for i in range(59):
        values.append((values[i] + values[i + 1]))

    idx = p_num % 60
    return_val = values[idx]
    return return_val


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
# 239 = 0
# 240 = 0