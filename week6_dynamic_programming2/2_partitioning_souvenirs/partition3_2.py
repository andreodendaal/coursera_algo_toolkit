# Uses python3
import sys
import itertools

def partition3(A):

    if sum(A) % 3 == 0:
        return 1
    else:
        return 0



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

# 11 17 59 34 57 17 23 67 1 18 2 59 = 1
# 4 3 3 3 3 = 0
# 13 1 2 3 4 5 5 7 7 8 10 12 19 25 = 1