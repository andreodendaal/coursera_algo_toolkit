# Uses python3
import sys
"""
Passed
"""
def get_change(money):
    #write your code here
    if money == 0:
        return 0
    coins = [1, 3, 4]
    numCoins = 0
    minNumCoins = {key: money for key in range(money + 1)}
    for m in range(1, money + 1):

        for i, coin in enumerate(coins):
            if m >= coin:
                if m % coin == 0:
                    numCoins = int(m/coin)
                else:
                    numCoins = minNumCoins.get(m - coin) + 1

                if numCoins < minNumCoins.get(m) and numCoins != 0:
                    minNumCoins[m] = numCoins

    final = minNumCoins.get(money)
    return final


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# 2 = 2
# 34 = 9
# 6 = 2