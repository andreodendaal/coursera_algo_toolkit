# Uses python3
import sys

def get_fibonacci_last_digit_ao(n):
    if n <= 1:
        return n

    #previous = 0
    #current  = 1
    values = [0, 1]

    for i in range(2,  (n + 1)):
        values.append(values[i - 1] + values[i - 2])

    return values[i] % 10

if __name__ == '__main__':
    #input = sys.stdin.read()
    #input_n = int(input())
    n = int(input())
    print(get_fibonacci_last_digit_ao(n))
