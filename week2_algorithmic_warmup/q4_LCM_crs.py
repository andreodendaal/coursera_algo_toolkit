# Uses python3
import sys


def lcm(a, b):
    vals = [a, b]
    lcm_val = max(vals)
    lcm_max = lcm_val
    lcm_min = min(vals)
    ctr = 2
    while (lcm_val % lcm_min) != 0:
        lcm_val = lcm_max * ctr
        ctr += 1

    return lcm_val


if __name__ == "__main__":
    #a = int(input())
    #b = int(input())
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

# 1 1000000
# 18 35 -> 630