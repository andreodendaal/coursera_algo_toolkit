#Uses python3

import sys

def largest_number(a):
    #write your code here
    bucket = []
    b9 = []
    b8 = []
    b7 = []
    b6 = []
    b5 = []
    b4 = []
    b3 = []
    b2 = []
    b1 = []
    merge = []

    res = ""

    for val in a:
        test = val[0]
        if int(test) == 1:
            b1.append(val)

        elif int(test) == 2:
            b2.append(val)

        elif int(test) == 3:
            b3.append(val)

        elif int(test) == 4:
            b4.append(val)

        elif int(test) == 5:
            b5.append(val)

        elif int(test) == 6:
            b6.append(val)

        elif int(test) == 7:
            b7.append(val)

        elif int(test) == 8:
            b8.append(val)

        elif int(test) == 9:
            b9.append(val)

        else:
            bucket.append(val)

    b1.sort()
    b2.sort()
    b3.sort()
    b5.sort()
    b6.sort()
    b7.sort()
    b8.sort()
    b9.sort()

    merge = b9 + b8 + b7 + b6 + b5 + b4 + b3 + b2 + b1

    for x in merge:
        res += str(x)
    #test_c = '9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010'
    #if res == test_c:
    #    yay = 1
    #if bucket != []:
    #    res = bucket
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

# 3 23 39 92 = 923923
# 6 9 4 91 6 1 9 = 99641
# 5 9 4 6 1 9 = 99641
# 2 21 2 = 221
# 3 3 155 22= 322155
# 4 3 9 3 155 = 933155
# 3 23 39 92 = 923923
# 100 2 8 2 3 6 4 1 1 10 6 3 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5
# 3 2 102 11 = 211102
# 4 2 8112 102 11