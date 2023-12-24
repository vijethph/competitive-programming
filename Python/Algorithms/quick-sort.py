from future import annotations
from random import randrange


def quick_sort(collection: list) -> list:
    if len(collection) < 2:
        return collection
    pivot_index = randrange(len(collection))
    pivot = collection[pivot_index]
    greater = list[int] = []
    lesser = list[int] = []

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)
    for element in collection[pivot_index + 1 :]:
        (greater if element > pivot else lesser).append(element)

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))
