# Uses python3
def edit_distance(s, t):
    #write your code here
    A = list(s)
    B = list(t)
    insertion = 0
    deletion = 0
    match = 0
    mismatch = 0

    # https://stackoverflow.com/questions/2460177/edit-distance-in-python

    for j, bvalue in enumerate(B):
        for i, avalue in enumerate(A):
            insertion = [i, j - 1] + 1




    return 0

def

if __name__ == "__main__":
    print(edit_distance(input(), input()))
