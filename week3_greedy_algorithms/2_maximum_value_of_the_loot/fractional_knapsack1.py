# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    buckets = []
    total_weights = 0
    total_values = 0

    for idx, weight in enumerate(weights):
        rem = capacity - weight
        item_value = values[idx]
        if rem == 0:
            buckets.append([capacity, item_value])

        elif len(buckets) == 0:
            buckets.append([rem, item_value])

        else:
            added = 0
            for ctx, values[0] in enumerate(buckets):
                if weight == values[ctx][0]:
                    buckets[ctx][0] = buckets[ctx][0] + rem
                    buckets[ctx][1] = buckets[ctx][1] + item_value
                    added = 1
                    break
            if added == 0:
                buckets.append([rem, item_value])




    return value








if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# 3 50 60 20 100 50 120 30 = 180.0000