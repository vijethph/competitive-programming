from __future__ import annotations

precision = 10


def linear_search(left: int, right: int, array: list[int], target: int) -> int:
    for i in range(left, right):
        if array[i] == target:
            return i
    return -1


def iterative_ternary_search(array: list[int], target: int) -> int:
    left = 0
    right = len(array)
    while left <= right:
        if right - left < precision:
            return linear_search(left, right, array, target)

        one_third = (left + right) // 3 + 1
        two_third = 2 * (left + right) // 3 + 1

        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third

        elif target < array[one_third]:
            right = one_third - 1
        elif target > array[two_third]:
            left = two_third + 1

        else:
            left = one_third + 1
            right = two_third - 1
    else:
        return -1


def recursive_ternary_search(left: int, right: int, array: list[int], target: int) -> int:
    if left < right:
        if right - left < precision:
            return linear_search(left, right, array, target)

        one_third = (left + right) // 3 + 1
        two_third = 2 * (left + right) // 3 + 1

        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third

        elif target < array[one_third]:
            return recursive_ternary_search(left, one_third - 1, array, target)
        elif target > array[two_third]:
            return recursive_ternary_search(two_third + 1, right, array, target)

        else:
            return recursive_ternary_search(one_third + 1, two_third - 1, array, target)
    else:
        return -1


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    array = [int(item.strip()) for item in user_input.split(",")]
    target = int(input("Enter a single number to be found in the list:\n").strip())
    result = iterative_ternary_search(array, target)
    if result != -1:
        print(f"{target} found at positions: {result}")
    else:
        print("Not found")
    result = recursive_ternary_search(0, len(array), array, target)
    if result != -1:
        print(f"{target} found at positions: {result}")
    else:
        print("Not found")
