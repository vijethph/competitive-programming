# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    
    def binSearch(self, nums, target, leftBias):
        # leftBias = True or False. if False, res is rightBiased
        left, right = 0, len(nums) - 1
        idx = -1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                idx = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return idx

