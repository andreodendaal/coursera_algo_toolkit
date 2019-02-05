# Uses python3
import sys
import operator

def get_optimal_value(capacity, weights, values):
    value = 0.
    buckets = []
    percent = 0.
    w = capacity

    for idx, val in enumerate(values):
        vw_weight = weights[idx]
        vw = val / vw_weight
        buckets.append([vw, vw_weight, val])
        buckets.sort(key=operator.itemgetter(0), reverse=True)

    ctr = 0
    while w > 0 and ctr < len(buckets):

        valueByWeight = buckets[ctr][0]
        itemWeight = buckets[ctr][1]
        itemValue = buckets[ctr][2]

        if itemWeight <= w:
            w -= itemWeight
            value += valueByWeight * itemWeight
        elif itemWeight > w:
            percentage = w/itemWeight
            value += percentage * itemValue
            w -= itemWeight * percentage
        ctr += 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# 3 5 20 4 14 2 18 3  = 32
# 3 50 60 20 100 50 120 30 = 180.0000
# 1 10 500 30 = 166.6667
# 3 10 1 9 2 9 1 9 = 2.111
# 1 1000 500 30 = 500.000
# 6/13 = 7777.731
# 3 50 60 20 60 15 120 30 = 195