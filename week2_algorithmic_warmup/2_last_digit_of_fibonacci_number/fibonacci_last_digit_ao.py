# Uses python3
import sys

def get_fibonacci_last_digit_ao(n):
    if n <= 1:
        return n

    #previous = 0
    #current  = 1
    values_from = (0, 1)

    for i in range(2,  (n + 1)):
        values_to = (values_from[1],(values_from[1] + values_from[0]))
        #values_to.append(values_from[1])
        #values_to.append((values_from[1] + values_from[0]))
        values_from = values_to[:]

    return values_to[1] % 10

if __name__ == '__main__':
    #input = sys.stdin.read()
    #input_n = int(input())
    n = int(input())
    print(get_fibonacci_last_digit_ao(n))
