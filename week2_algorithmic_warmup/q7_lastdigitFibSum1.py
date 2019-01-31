# Uses python3
import sys

def q7_lastdigitFibSum(p_start, p_num):

    if p_num <= 2:
        return p_num

    values = [0, 1]
    total = [0]

    m_start = p_start % 60
    m_num = p_num % 60

    for i in range(59):

        values.append((values[i] + values[i + 1]))

        if i + 2 >= m_start:
            total.append((sum(values[m_start:]) % 10))

        if i + 2 == m_num:
            return total[-1]

    return_total = total[-1]
    return return_total


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(q7_lastdigitFibSum(a, b))

# 1234 12345 = 8
# 3 7 = 1
# 10 10 = 5
