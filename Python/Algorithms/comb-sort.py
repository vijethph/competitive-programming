def comb_sort(data: list) -> list:
    shrink_factor = 1.3
    gap = len(data)
    completed = False

    while not completed:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            completed = True

        index = 0
        while index + gap < len(data):
            if data[index] > data[index + gap]:
                data[index], data[index + gap] = data[index + gap], data[index]
                completed = False
            index += 1

    return data


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(comb_sort(unsorted))
