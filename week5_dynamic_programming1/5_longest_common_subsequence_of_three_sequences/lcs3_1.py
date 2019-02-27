#Uses python3

# Tabulation approach

import sys

def lcs2(X, Y):
    #write your code here
    if len(Y) > len(X):
        X, Y = Y, X
    x = len(X)
    y = len(Y)

    # declaring the array for storing the dp values
    L = [[0] * (y + 1) for i in list(range(x + 1))]
    #L = [[None] * (x + 1) for i in list(range(y + 1))]

    for x_i in range(x + 1):
        for y_i in range(y + 1):
            if x_i == 0 or y_i == 0:
                L[x_i][y_i] = 0
            elif X[x_i - 1] == Y[y_i - 1]:
                L[x_i][y_i] = L[x_i - 1][y_i - 1] + 1
            else:
                L[x_i][y_i] = max(L[x_i - 1][y_i], L[x_i][y_i - 1])

    answer = L[x][y]
    return answer


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

# 3 2 7 5  2 2 5 = 2
# 1 7  4 1 2 3 4 = 0
# 4 2 7 8 3  4 5 2 8 7 = 2
