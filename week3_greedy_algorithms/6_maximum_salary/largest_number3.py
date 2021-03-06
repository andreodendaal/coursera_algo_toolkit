#Uses python3

import sys
from collections import deque

def largest_number(a):
    #write your code here

    def maxDigits(value):
        # A value of 7 is greater than 75 or 76 and should be selected first. 775 > 757
        # But 77 upward would be greater 78 should come before the single digit 7. 787 > 778
        if int(value) >= 10 and int(value) < 100:

            if value[-1] >= value[-2]:
                return value

            elif value[-1] < value[-2] and value[-2] in digits:
                return value[0]

            else:
                return value

        elif int(value) >= 100 and int(value) < 1000:

        else:
            return value

    res = ""
    digits = deque(a[:])
    orderedDigits = []

    while digits:
        # get largest value but test
        maxdigit = maxDigits(max(digits))
        orderedDigits.append(maxdigit)
        digits.remove(maxdigit)

    for x in orderedDigits:
        res += x

    return res



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

# 4 71 73 79 7 = 7977371
# 2 21 2 = 221
# 3 3 155 22= 322155
# 4 3 9 3 155 = 933155
# 3 23 39 92 = 923923
# 100 2 8 2 3 6 4 1 1 10 6 3 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5
