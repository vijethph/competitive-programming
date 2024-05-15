# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        for i, num in enumerate(nums):
            if num >= target:
                return i
        
        return len(nums)

        # alternative solution
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left