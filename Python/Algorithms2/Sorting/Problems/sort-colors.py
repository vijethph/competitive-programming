# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, arr, start, end):
        if end - start + 1 <= 1:
            return arr
        
        pivot = arr[end]
        left = start

        for i in range(start, end):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        arr[end] = arr[left]
        arr[left] = pivot

        self.quickSort(arr, start, left - 1)
        self.quickSort(arr, left + 1, end)

        return arr