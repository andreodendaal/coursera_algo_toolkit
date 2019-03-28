# Uses python3
import sys

def optimal_weight(W, lst_bars):
    # write your code here
    weights_row = [0 for i in range(W)]
    weights_grid = []
    weights_grid.append(weights_row)
    result = 0

    bar_processed = [0]
    for i in range(len(lst_bars)):

        weights_row = []
        w = 0

        while w < W:
            w_bar = lst_bars[i]

            if w_bar == w:
                weights_row.append(w_bar)

            elif w_bar < w:

                bar_tot = 0
                bar_prev_tot = 0

                for previous_bar in bar_processed:

                    bar_test = w_bar + previous_bar

                    if bar_test == w:
                        bar_tot = bar_test

                    elif bar_test < weights_grid[i][w] and bar_test > bar_tot:
                        bar_tot = weights_grid[i][w]

                    elif bar_test <= w and bar_test > bar_prev_tot:
                        bar_tot = bar_test
                        bar_prev_tot = bar_test

                    elif previous_bar == w:
                        bar_tot = previous_bar
                        bar_prev_tot = bar_tot

                weights_row.append(bar_tot)

            else:
                test = weights_grid[i][w]
                weights_row.append(test)

            w += 1

        bar_processed.append(lst_bars[i])

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