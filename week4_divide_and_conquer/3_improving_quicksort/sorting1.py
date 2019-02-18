# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    ref, left, right = a[l], l, r
    i = l

    while i <= right:
        if a[i] < ref:
            a[left], a[i] = a[i], a[left]
            left += 1

        elif a[i] > ref:
            a[right], a[i] = a[i], a[right]
            right -= 1
            i -= 1  # remain in the same i in this case
        i += 1
    return left, right

def partition2(a, l, r):
    x = a[l]
    j = l
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
    left, right = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, right - 1);
    randomized_quick_sort(a, left + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

# 5 2 3 9 2 2 = 2 2 2 3 9