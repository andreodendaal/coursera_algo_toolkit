#Uses python3

import sys
from collections import deque

def largest_number(a):
    #write your code here

    def digitTest(p_max, p_read):
        maxlen = len(max(a))
        v_max = int(p_max)*(maxlen * 2 // len(p_max))
        v_read = int(p_read) * (maxlen * 2 // len(p_read))
        print('hello')

    res = ""
    digits = deque(a[:])
    orderedDigits = []
    maxdigit = 999
    ctr = 1
    while digits:

        for digit in digits:

            if digitTest(str(maxdigit), digit):
                maxdigit = int(digit)
                orderedDigits.append(digit)
                digits.remove(digit)
                break
            else:
                maxdigit -= ctr



    for x in orderedDigits:
        res += x

    return res



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

# 5 71 73 79 7 98 = 987977371
# 2 21 2 = 221
# 3 3 155 22= 322155
# 4 3 9 3 155 = 933155
# 3 23 39 92 = 923923
# 100 2 8 2 3 6 4 1 1 10 6 3 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5
