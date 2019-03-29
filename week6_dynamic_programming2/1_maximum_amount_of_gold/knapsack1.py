# Uses python3
import sys

def optimal_weight(W, lst_bars):
    # write your code here
    weights_row = [0 for i in range(W + 1)]
    weights_grid = []
    weights_grid.append(weights_row)
    bar_processed = [0]
    lst_bars.sort()

    for bar_ctr, latest_bar in enumerate(lst_bars):

        weights_row = []

        bar_tot = 0
        #optimal = 0

        for weight, prev_weight in enumerate(weights_grid[-1]):
            # process current weight
            if latest_bar == weight:
                weights_row.append(latest_bar)

            elif latest_bar < weight:

                # process current weight
                optimal_with_latest = latest_bar
                bar_tot = latest_bar
                for prev_bar in bar_processed:
                    bar_tot += prev_bar

                    if bar_tot <= weight:
                        if bar_tot > optimal_with_latest:
                            optimal_with_latest = bar_tot

                    elif optimal_with_latest <= weight and bar_tot > weight:
                        optimal_with_latest = optimal_with_latest

                    else:
                        optimal_with_latest = latest_bar

                optimal_with_previous = bar_processed[-1]
                bar_tot = 0

                for prev_bar in bar_processed:
                    bar_tot += prev_bar

                    if bar_tot <= weight:
                        if bar_tot > optimal_with_previous:
                            optimal_with_previous = bar_tot

                    elif optimal_with_previous <= weight and bar_tot > weight:
                        optimal_with_previous = optimal_with_previous

                    else:
                        optimal_with_previous = bar_processed[-1]

                if optimal_with_latest > optimal_with_previous:
                    optimal = optimal_with_latest
                else:
                    optimal = optimal_with_previous

                weights_row.append(optimal)

            else:
                weights_row.append(prev_weight)

        bar_processed.append(latest_bar)

        weights_grid.append(weights_row)

        #for bar in lst_bars:
        #    if result + bar <= W:
        #        result = result + bar

    result = weights_grid[-1][-1]
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


# 10 3 1 4 8 = 9
# 10 3 4 1 8 = 9
# 10 3 8 1 4 = 9
# 10 3 8 4 1 = 9
# 10 4 8 2 4 1 = 10
# 11 4 8 2 4 1 = 11
# 101 3 100 1 2 = 101
# 11 3 10 1 2 = 11
# 101 3 100 3 2 = 100
# 20 4 5 7 12 18 = 19