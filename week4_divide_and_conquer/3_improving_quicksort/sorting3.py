# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x, j, t = a[l], l, r
    i = j
    #print(ref)
    while i <= t:
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1
            print(f'Less than ref {x} {a}')

        elif a[i] > x:
            a[t], a[i] = a[i], a[t]
            t -= 1
            i -= 1  # remain in the same i in this case
            print(f'Greater than ref {x} {a}')
        i += 1


    return j, t

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r, ref):
    if l >= r:
        return
    print(ref)
    k = random.randint(l, r)
    print(f'reference k: {k}')
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    #m = partition2(a, l, r)
    ref1 = 'm1 -1 call'
    randomized_quick_sort(a, l, m1 - 1, ref1);
    ref2 = 'm2 + 1 call'
    randomized_quick_sort(a, m2 + 1, r, ref2);


if __name__ == '__main__':
    input = sys.stdin.read()



    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1, 'first call')
    for x in a:
        print(x, end=' ')

# 5 2 3 9 2 9 = 2 2 3 9 9
# 10 10 9 8 7 6 5 4 3 2 1 = 1 2 3 4 5 6 7 8 9 10
