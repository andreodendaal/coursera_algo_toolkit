# Uses python3
import sys

def get_change(money):
    #write your code here
    minNumCoins = []
    for m in range(money + 1):
        minNumCoins.append(m)


    return minNumCoins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

#