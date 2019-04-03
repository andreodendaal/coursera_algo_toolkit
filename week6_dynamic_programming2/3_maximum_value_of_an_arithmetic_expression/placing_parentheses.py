# Uses python3

#Pass
import re

#use eval
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    global max_grid
    global min_grid

    lst_dataset = list(dataset)
    str_integers = (re.sub("\D", "", dataset))
    str_operators = ''.join(i for i in dataset if not i.isdigit())

    leng = len(str_integers)
    max_grid = [[0] * len(str_integers) for _ in range(leng)]
    min_grid = [[0] * len(str_integers) for _ in range(leng)]

    # Build initial 2D lists building the main diagonal using initial values
    #Max grid
    for ctr, val in enumerate(str_integers):
        max_grid[ctr][ctr] = int(val)

    for ctr, val in enumerate(str_integers):
        min_grid[ctr][ctr] = int(val)

    for l, val in enumerate(str_integers, start=1):
    #for l, val in enumerate(str_integers):

        for i in range(leng - l):
        #for i in range(leng - 1):
        #i = 0
        #while i < (leng - l):
            min_tmp = []
            max_tmp = []

            #j = i + (l + 1)
            j = i + l
            k = i

            while k < j:
                if str_operators[k] == '+':
                    min_tmp.append(min_grid[i][k] + min_grid[k + 1][j])
                    max_tmp.append(max_grid[i][k] + max_grid[k + 1][j])
                    min_tmp.append(min_grid[i][k] + max_grid[k + 1][j])
                    max_tmp.append(max_grid[i][k] + min_grid[k + 1][j])
                elif str_operators[k] == '-':
                    min_tmp.append(min_grid[i][k] - min_grid[k + 1][j])
                    max_tmp.append(max_grid[i][k] - max_grid[k + 1][j])
                    min_tmp.append(min_grid[i][k] - max_grid[k + 1][j])
                    max_tmp.append(max_grid[i][k] - min_grid[k + 1][j])
                elif str_operators[k] == '*':
                    min_tmp.append(min_grid[i][k] * min_grid[k + 1][j])
                    max_tmp.append(max_grid[i][k] * max_grid[k + 1][j])
                    min_tmp.append(min_grid[i][k] * max_grid[k + 1][j])
                    max_tmp.append(max_grid[i][k] * min_grid[k + 1][j])

                k += 1


            max_amt = max(max_tmp)
            old_maxval = max_grid[i][j]
            max_grid[i][j] = max_amt
            min_amt = min(min_tmp)
            min_grid[i][j] = min_amt

            #i += 1

    final = max_grid[0][-1]
    return final


def MinandMax(i, j):
    min = 0
    max = 0
    param_range = len(range(j-1))
    for k in range(param_range):
        valueM = max_grid[i][k]



if __name__ == "__main__":
    print(get_maximum_value(input()))

# 5-8+7*4-8+9 = 200
# 1+2*3+4*5 = 105

