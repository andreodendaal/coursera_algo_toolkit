# Uses python3
import sys

def get_fibonacci_last_digit_efficient(n):
    if n <= 1:
        return n
    values_mod = []
    values = [0, 1]
    for i in range(2,  (n + 1)):
        values.append(values[i - 1] + values[i - 2])
        values_mod.append((values[i] % 3))

    print(values_mod)

    return values[i] % 3



if __name__ == '__main__':
    #input = sys.stdin.read()
    #input_n = int(input())
    n = int(input())
    print(get_fibonacci_last_digit_efficient(n))
