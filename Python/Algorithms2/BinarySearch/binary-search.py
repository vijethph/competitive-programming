class BinarySearch:
    def binary_search(array, target):
        left, right = 0, len(array) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if target > array[mid]:
                left = mid + 1
            elif target < array[mid]:
                right = mid - 1
            else:
                return mid
        
        return -1
            