# Uses python3
import sys

# http://bitingcode.blogspot.com/2016/12/knapsack-without-repetition.html
# https://codereview.stackexchange.com/questions/20569/dynamic-programming-knapsack-solution
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://stackoverflow.com/questions/36348662/discrete-knapsack-dynamic-programming-python3
def optimal_weight(W, lst_bars):

    # write your code here
    lst_bars.sort(reverse=True)
    candidates = []

    for i in range(len(lst_bars)):
        total = 0
        candidate = 0

        bar_processing = lst_bars[i]

        for bar in lst_bars[i:]:

            total += bar

            if total == W:

                candidate = total

            elif total < W:

                if total > candidate:
                    candidate = total

            elif total > W:

                # Reset to the value of the current bar. To process the next item
                if bar_processing < W:
                    total = bar_processing
                else:
                    total = 0

        candidates.append(candidate)

    return max(candidates)


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
# 20 4 21 5 6 1  = 12
# 20 5 21 5 6 1 4  = 16