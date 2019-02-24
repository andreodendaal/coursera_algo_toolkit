# Uses python3

# Passed

def edit_distance(side, top):
    #write your code here
    if len(side) > len(top):
        top, side = side, top

    previous_row = list(range(len(top) + 1))

    for idx_side, c_side in enumerate(side):
        current_row = [idx_side + 1]

        for idx_top, c_top in enumerate(top):
            if c_top == c_side:
                current_row.append(previous_row[idx_top])

            else:
                above_left = previous_row[idx_top]
                above = previous_row[idx_top + 1]
                left = current_row[-1]
                current_row.append(1 + min((above_left, above, left)))

        previous_row = current_row

    return previous_row[-1]

if __name__ == "__main__":
    #edit_distance(input(), input())
    print(edit_distance(input(), input()))
