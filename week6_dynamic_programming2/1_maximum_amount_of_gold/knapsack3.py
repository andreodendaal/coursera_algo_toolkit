# Uses python3
import sys

# http://bitingcode.blogspot.com/2016/12/knapsack-without-repetition.html
# https://codereview.stackexchange.com/questions/20569/dynamic-programming-knapsack-solution
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# https://stackoverflow.com/questions/36348662/discrete-knapsack-dynamic-programming-python3
# https://github.com/ayanmaj92/algorithm_specialisation/blob/master/1.Algorithmic_Toolbox/5.Dynamic_Programming/knapsack.py

# https://towardsdatascience.com/course-1-algorithmic-toolbox-part-4-dynamic-programming-223ffc01984a

def optimal_weight(W, lst_bars):

    if W > 10**4:
        return 0
    elif len(lst_bars) > 300:
        return 0


    # write your code here
    lst_bars.sort(reverse=True)
    #lst_bars.sort()
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
                if bar_processing <= W:
                    #total = bar_processing
                    if bar_processing >= candidate:
                        total = bar_processing

                    else:
                        total = candidate

                else:
                    total = 0

        candidates.append(candidate)

    return max(candidates)


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

# 5 4 6 3 4 2 = 5
# 10 4 6 3 4 2 = 10
# 20 10 9 8 8 6 6 6 5 5 4
# 10 5 3 5 3 3 5 = 10
# 30 3 19 5 4
# 19 4 9 35 35 40 = 9
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

# 20 6 16 21 5 6 1 4  = 16

# 20 6 12 6 5 3 2 1 = 20
# 20 4 21 25 5 22 = 5
# 20 5 21 4 25 5 22 = 9

