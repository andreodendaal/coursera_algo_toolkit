# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        mod3 = n % 3
        floor3 = n // 3
        mod2 = n % 2
        floor2 = n // 2

        if n == 10 and (n - 1) % 3 == 0:
            n = n - 1
            sequence.append(n)

        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# 1 = 0 1
# 96234 = 14    1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
# or      14    1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117 96234
#               1 2 6 7  21 22 66 198 594 1782 5346 16038 16039 32078 96234
# wrong   15  1 2 4 5 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234