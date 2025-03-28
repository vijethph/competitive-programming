# stable sorting algorithms - preserve the original ordering of elements in the case of duplicates
# unstable sorting algorithms - may not preserve the ordering of elements in the case of duplicates

# insertion sort is stable sorting algorithm - O(n^2) - iterative approach
# divide into subproblems i.e., sort the first 2 elements, the first 3 elements and so on ...

class InsertionSort:
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                # arr[j] and arr[j + 1] are out of order so swap them
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                j -= 1

        return arr
