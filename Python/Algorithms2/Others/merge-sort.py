# divide and conquer: divide problem space into 2 halves and merge the sorted halves

# time: O(nlogn)
# space: O(n)
# stable sort

class MergeSort:
    def merge_sort(arr, start, end):
        if end - start + 1 <= 1: # calculate length of subarray
            return arr
        
        mid = (start + end) // 2

        merge_sort(arr, start, mid) # left half
        merge_sort(arr, mid + 1, end) # right half

        merge(arr, start, mid, end) # merge sorted halves

        return arr
    
    def merge(arr, start, mid, end):
        # copy the left and right halves to temporary arrays
        left = arr[start:mid + 1]
        right = arr[mid + 1: end + 1]

        i = 0 # index for left
        j = 0 # index for right
        k = start # index for arr

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left): # put the remaining elements, if there are any
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right): # put the remaining elements, if there are any
            arr[k] = right[j]
            j += 1
            k += 1
        



