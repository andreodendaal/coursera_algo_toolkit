def get_pisano(modulo):

    previous = 1
    current = 1

    result = 1
    while not (previous == 0 and current == 1):  # 1
        buffer = (previous + current) % modulo  # 2
        previous = current
        current = buffer

        result += 1

    return result

print(get_pisano(10))