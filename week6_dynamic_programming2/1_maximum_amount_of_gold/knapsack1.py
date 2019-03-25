# Uses python3
import sys

def optimal_weight(W, lst_bars):
    # write your code here
    weights_row = [0 for i in range(W)]
    weights_grid = []
    weights_grid.append(weights_row)
    result = 0
    previous_bar = 0
    for i in range(len(lst_bars)):
        weights_row = []
        w = 0
        while w <= W:
            w_bar = lst_bars[i]
            if w_bar <= w:
                weights_row.append(w_bar)

            else:
                test = weights_grid[i][w]
                weights_row.append(test)


            w += 1
        weights_grid.append(weights_row)

        #for bar in lst_bars:
        #    if result + bar <= W:
        #        result = result + bar

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


# 10 3 1 4 8 = 9