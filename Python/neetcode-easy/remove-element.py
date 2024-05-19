# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]

        return len(nums)

        # alternative solution
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                # partition the array
                nums[k] = nums[i]
                k += 1
        return k