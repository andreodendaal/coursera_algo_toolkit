# Uses python3
import re

#use eval
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    global max_grid
    global min_grid

    lst_dataset = list(dataset)
    str_integers = (re.sub("\D", "", dataset))
    str_operators = ''.join(i for i in dataset if not i.isdigit())
    #lst_integers = list(int(str_integers))
    n = len(str_integers)
    max_grid = [[0] * len(str_integers) for _ in range(n)]

    for ctr, val in enumerate(str_integers):
        max_grid[ctr][ctr] = val

    min_grid = max_grid[:]

    for s, val in enumerate(str_integers, start=1):
        param_range = n - s
        for (i) in range(1, n - s):
            j = i + s
            print(i)
            #MinandMax(i, j)

    return 0


def MinandMax(i, j):
    min = 0
    max = 0
    param_range = len(range(j-1))
    for k in range(param_range):
        valueM = max_grid[i][k]



if __name__ == "__main__":
    print(get_maximum_value(input()))

# 5-8+7*4-8+9 = 200

# https://www.geeksforgeeks.org/minimum-maximum-values-expression/