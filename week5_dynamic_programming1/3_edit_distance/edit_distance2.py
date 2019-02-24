# Uses python3

# not working

def edit_distance(side, top):
    #write your code here
    if len(side) > len(top):
       top, side = side, top


    previous_row = list(range(len(top) + 1))

    for i_side, c_side in enumerate(side):
        this_row = [i_side + 1]

        for i_top, c_top in enumerate(top):

            insertion = previous_row[i_top + 1] + 1
            deletion = this_row[i_top] + 1
            match = (i_top - 1) + (i_side - 1)
            test = c_side != c_top
            mismatch = previous_row[i_top] + (c_side != c_top)

            if c_top == c_side:
                this_row.append(min(insertion, deletion, match))
            else:
                this_row.append(min(insertion, deletion, mismatch))
        previous_row = this_row
    answer = previous_row[-1]
    return previous_row[-1]

if __name__ == "__main__":
    #edit_distance(input(), input())
    print(edit_distance(input(), input()))
