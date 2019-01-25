# Uses python3
import sys
import math


def lcm(a, b):
    p_gcd = int(math.gcd(int(a), int(b)))
    lcm_val = int(int(a) * int(b))
    lcm_return = int(int(lcm_val)/int(p_gcd))
    return int(lcm_return)


if __name__ == "__main__":
    #a = int(input())
    #b = int(input())
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

# 1 1000000
# 18 35 -> 630
# 226553150 1023473145 -> 46374212988031350 ctr 45310630