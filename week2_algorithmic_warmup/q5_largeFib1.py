# Uses python3
import sys


def large_fib(func_value, mod):

    values = [0, 1]
    ctr = 0
    mod_value = 0

    while mod_value == 0:
        values.append((values[ctr] + values[ctr + 1]) % mod)
        ctr += 1
        if values[-2:] == [0, 1]:
            mod_value = ctr

    remainder = func_value % mod_value

    return values[remainder]


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(large_fib(a, b))

# 1 1000000
# 18 35 -> 630 ctr 18
# 226553150 1023473145 -> 46374212988031350 ctr 45310630