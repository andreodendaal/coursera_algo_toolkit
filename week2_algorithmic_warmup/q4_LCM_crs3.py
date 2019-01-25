# Uses python3
import sys
import math


def lcm(a, b):
    gcd = int(math.gcd(a, b))

    
    lcm_val = int(a * b)
    lcm_return = lcm_val/gcd
    return lcm_return


if __name__ == "__main__":
    #a = int(input())
    #b = int(input())
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

# 1 1000000
# 18 35 -> 630