
def euclidGCD (a, b):

    if b == 0:
        return a

    remainder = a % b
    print(b, remainder)
    return euclidGCD(b, remainder)


print(euclidGCD(357, 234))