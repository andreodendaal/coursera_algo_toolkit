# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    numberOfItems = capacity
    maxCapacity = capacity
    options = []
    idx = 0
    ctr = 0
    registry = []
    while weights:
        if maxCapacity in weights:
            idx = weights.index(maxCapacity)
            options.append([values[idx], maxCapacity])
            weights.remove(maxCapacity)
            values.pop(idx)
            registry.append(values[idx])
            ctr += 1

        next_load = [0, 0]
        for load in range(len(capacity)):
            if next_load != maxCapacity:
                next_load[1] =










    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# 3 50 60 20 100 50 120 30 = 180.0000