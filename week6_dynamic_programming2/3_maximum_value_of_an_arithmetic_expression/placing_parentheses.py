# Uses python3
import re

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
    lst_integers = re.sub("\D", "", dataset)
    n = len(lst_integers)
    max_grid = [[0] * len(lst_integers) for _ in range(n)]

    for ctr, val in enumerate(lst_integers):
        max_grid[ctr][ctr] = val
    min_grid = max_grid[:]

    for s in range(n - 1):
        for i in range(n - s):
            j = i + s
            MinandMax(i, j)

    return 0


def MinandMax(i, j):
    print(max_grid)


if __name__ == "__main__":
    print(get_maximum_value(input()))

# 5-8+7*4-8+9 = 200