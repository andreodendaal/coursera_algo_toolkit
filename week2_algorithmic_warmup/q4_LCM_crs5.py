# Uses python3
import sys
import math

# define lcm function
def f_lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""
    lcm = (x * y) // (math.gcd(int(a), int(b)))
    return lcm


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(f_lcm(a, b))

# 1 1000000
# 18 35 -> 630 ctr 18
# 226553150 1023473145 -> 46374212988031350 ctr 45310630