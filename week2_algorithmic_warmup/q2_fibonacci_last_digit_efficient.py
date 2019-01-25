# Uses python3
import sys

def get_fibonacci_last_digit_efficient(n):
    if n <= 1:
        return n
<<<<<<< HEAD:week2_algorithmic_warmup/2_last_digit_of_fibonacci_number/fibonacci_last_digit_ao.py

    #previous = 0
    #current  = 1
    values_from = (0, 1)

    for i in range(2,  (n + 1)):
        values_to = (values_from[1],(values_from[1] + values_from[0]))
        #values_to.append(values_from[1])
        #values_to.append((values_from[1] + values_from[0]))
        values_from = values_to[:]

    return values_to[1] % 10
=======
    values_mod = []
    values = [0, 1]
    for i in range(2,  (n + 1)):
        values.append(values[i - 1] + values[i - 2])
        values_mod.append((values[i] % 3))

    print(values_mod)

    return values[i] % 3


>>>>>>> a27e2fe20e589fdcb5345c4e9a7a388c128e5926:week2_algorithmic_warmup/q2_fibonacci_last_digit_efficient.py

if __name__ == '__main__':
    #input = sys.stdin.read()
    #input_n = int(input())
    n = int(input())
    print(get_fibonacci_last_digit_efficient(n))
