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
    lst_dataset = list(dataset)
    integers = re.sub("\D", "", dataset)
    max_grid = [[0] * len(integers) for _ in range(len(integers))]

    for ctr, val in enumerate(integers):
        max_grid[ctr][ctr] = val

    min_grid = max_grid[:]

    return 0


if __name__ == "__main__":
    print(get_maximum_value(input()))

# 5-8+7*4-8+9 = 200