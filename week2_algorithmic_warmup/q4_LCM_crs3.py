# Uses python3
import sys
import math


def lcm(a, b):

    vals = [a, b]
    vals.sort()
    LCM = vals[1]

    ctr = 2
    while LCM % vals[0] != 0:
        LCM = vals[1] * ctr
        ctr += 1

    return LCM, ctr - 1


if __name__ == "__main__":
    #a = int(input())
    #b = int(input())
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

# 1 1000000
# 18 35 -> 630 ctr 18
# 226553150 1023473145 -> 46374212988031350 ctr 45310630