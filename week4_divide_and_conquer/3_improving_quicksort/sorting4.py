# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x, j, t = a[l], l, r

    for i, elem in enumerate(a):
        if elem < x:

            a[i], a[j] = a[j], a[i]
            j += 1


        elif elem > x:

            a[t], a[i] = a[i], a[t]
            t -= 1


    return j, t

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

# 5 2 3 9 2 9 = 2 2 3 9 9
# 10 10 9 8 7 6 5 4 3 2 1 = 1 2 3 4 5 6 7 8 9 10
