# Uses python3
import sys

def get_majority_element(a, left, right):
    a.sort()
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid1 = right/2
    mid2 = right // 2
    if a.count(a[mid2]) > mid1:
        return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

# 5 2 3 9 2 2 = 1
# 5 3 9 2 2 2 = 1
# 5 3 2 2 2 9 = 1
# 4 1 2 3 4 = 0
# 4 1 2 3 1 = 0
