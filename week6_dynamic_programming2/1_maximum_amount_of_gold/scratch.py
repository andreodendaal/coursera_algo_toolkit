# 5 7 12 18 = 19
from itertools import combinations

def find_sum_in_list(numbers, target):
    results = []
    for x in range(len(numbers)):
        results.extend(
            [
                combo for combo in combinations(numbers, x) if sum(combo) <= target
            ]
        )

    print(results)

if __name__ == "__main__":
    find_sum_in_list([5, 7, 12, 18], 18)