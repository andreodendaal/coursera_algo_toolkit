# Uses python3
import sys


def q7_lastdigitFibSum(p_start, p_num):

    if p_num <= 2:
        return p_num

    values = [0, 1]
    total = [0]


    for i in range(59):

        values.append((values[i] + values[i + 1]))
        if i + 2 >= p_start:
            total.append((sum(values[p_start:]) % 10))

        if i + 2 == p_num:
            return total[-1]

    idx = p_num % 60
    return_total = total[idx]
    return return_total


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(q7_lastdigitFibSum(a, b))

# 100 = 5
# sum of 100  = 927372692193078999175.
# 101th value = 927372692193078999176
# 100 th value = 573147844013817084101
# sum of 50 =    32951280098
# 51 th value =  32951280099
# 239 = 0
# 240 = 0