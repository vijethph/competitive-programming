# similar to merge sort, but we pick a random element called pivot (usually the last element)
# compare every other value with pivot and put it in left or right halves based on values
# in-place unstable sort, no additional memory allocation
# time: O(nlogn) if pivot is picked properly (first, last, middle or random)
# space: O(n)

class QuickSort:
    def quick_sort(arr, start, end):
        if end - start + 1 <= 1: # calculate length of subarray
            return arr

        pivot = arr[end] # last element is pivot
        left = start # pointer for left side

        for i in range(start, end):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # swap the pivot element to the correct position
        arr[end] = arr[left]
        arr[left] = pivot 

        quick_sort(arr, start, left - 1) # left half excluding pivot
        quick_sort(arr, left + 1, end) # right half excluding pivot

        return arr


