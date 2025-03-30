# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointers - left and right at the ends of the array to find elements in largest to smallest order - descending
        res = []
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res.append(nums[left] * nums[left])
                left += 1
            else:
                res.append(nums[right] * nums[right])
                right -= 1

        return res[::-1]