# Uses python3

def fib(n):
    if n <= 1:
        return n

    values = [0, 1]
    for i in range(2,  (n + 1)):
        values.append((values[i - 1] + values[i - 2]) % 10)

    return values[i]



if __name__ == '__main__':
    n = int(input())
    print(fib(n))
