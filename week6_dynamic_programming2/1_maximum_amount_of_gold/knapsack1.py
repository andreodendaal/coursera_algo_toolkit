# Uses python3
import sys

def optimal_weight(W, lst_bars):
    # write your code here
    weights_row = [0 for i in range(W + 1)]
    weights_grid = []
    weights_grid.append(weights_row)
    bar_processed = [0]
    lst_bars.sort()

    for bar in lst_bars:

        weights_row = []
        for w in weights_grid[i]:

            if bar == w:
                weights




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
# 10 4 8 2 4 1 = 10
# 11 4 8 2 4 1 = 11