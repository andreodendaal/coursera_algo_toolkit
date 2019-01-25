# Uses python3
import sys

def euclidGCD(a, b):

    if b == 0:
        return a

    remainder = a % b
    #print(b, remainder)
    return euclidGCD(b, remainder)

if __name__ == '__main__':
    #n1 = int(input())
    #n2 = int(input())
    input = sys.stdin.read()
    n1, n2 = map(int, input.split())
    print(euclidGCD(n1, n2))

#print(euclidGCD(357, 234))