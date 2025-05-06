# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1index = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]

            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1index[val]
                res[idx] = cur
            
            if cur in nums1index:
                stack.append(cur)
        
        return res