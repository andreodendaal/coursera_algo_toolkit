# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    buckets = []
    percent = 0.


    for idx, weight in enumerate(weights):
        rem = capacity - weight
        item_value = values[idx]

        # Bucket item at max capacity
        if rem == 0:
            buckets.append([capacity, item_value])

        # bucket first incomplete item
        elif len(buckets) == 0 and weight < capacity:
            buckets.append([rem, item_value])

        elif weight > capacity:
            percent_value = percentages(capacity, weight, item_value)
            buckets.append([capacity, percent_value])

        # process all fractions and allocate
        else:
            added = 0

            try:
                for ctx, bucket_values in enumerate(buckets):
                    bucket_weight = bucket_values[0]
                    if weight == bucket_weight:
                        buckets[ctx][0] = buckets[ctx][0] + rem
                        buckets[ctx][1] = buckets[ctx][1] + item_value
                        added = 1
                        break
            except Exception as ex:
                print(ex)

            if added == 0:
                buckets.append([rem, item_value])
    # get max value
    max_val = 0
    #process buckets and fill them with % if not 100% at capacity
    """
    for ftx, value_test in enumerate(buckets):
        # test = buckets[1]
        if value_test[0] != capacity:
            percent = percentages(value_test[0], capacity, value_test[1])
            buckets[ftx][0] = buckets[ftx][0] + (capacity - buckets[ftx][0])
            buckets[ftx][1] = float(buckets[ftx][1] + item_value * percent)
    """
    try:
        for btx, value2 in enumerate(buckets):
            #test = buckets[1]
            if value2[1] > max_val:
                max_val = value2[1]

    except Exception as ex:
        print(ex)

    value = float(max_val)

    return value

def percentages(capacity, weight, itemvalue):
    percent = (capacity / weight) * itemvalue
    return percent

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# 3 50 60 20 100 50 120 30 = 180.0000
# 1 10 500 30 = 166.6667
# 3 10 1 9 2 9 1 9 = 2.111
# 1 1000 500 30 = 500.000
# 6/13 = 7777.731
# 3 50 60 20 60 15 120 30 = 195