# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use 2 pointers to get close to the target
        # decrease right pointer everytime the sum > target
        # increment left pointer every time the sum < target
        left, right = 0, len(numbers) - 1
        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        