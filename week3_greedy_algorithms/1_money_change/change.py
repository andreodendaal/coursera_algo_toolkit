# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [10, 5, 1]
    running_total = m

    coin_total = 0
    denom_totalValue = 0

    for coin_value in coins:
        floor = running_total // coin_value
        coin_total += floor
        denom_totalValue = coin_value * floor
        running_total -= denom_totalValue

    return coin_total

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
