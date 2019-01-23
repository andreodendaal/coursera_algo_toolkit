# python3


def max_pairwise_product(lst_numbers):

    max_num1 = max(lst_numbers)
    lst_numbers.remove(max_num1)
    max_num2 = max(lst_numbers)
    max_product = max_num1 * max_num2

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
