# Uses python3


import sys

def binary_search(a, x):
    minIndex, maxIndex = 0, len(a) - 1
    # write your code here
    while maxIndex >= minIndex:
        midIndex = int((minIndex + maxIndex)/2)

        if a[midIndex] == x:
            return midIndex
        elif a[midIndex] < x:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end=' ')

# 5 1 5 8 12 13 5 8 1 23 1 11
