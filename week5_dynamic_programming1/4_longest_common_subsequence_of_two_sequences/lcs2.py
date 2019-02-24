#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    a_lst = list(a)
    b_lst = list(b)
    for i in a_lst:
        if i not in b_lst:
            a_lst.remove(i)

    for b in b_lst:
        if b not in a_lst:
            b_lst.remove(b)

    return min(len(a_lst), len(b_lst))


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
