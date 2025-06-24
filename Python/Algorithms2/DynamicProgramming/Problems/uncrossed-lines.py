# https://leetcode.com/problems/uncrossed-lines/description/

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # time: O(n * m)
        # space: O(m)

        prev = [0] * (len(nums2) + 1)

        for i in range(len(nums1)):
            dp = [0] * (len(nums2) + 1)

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[j + 1] = 1 + prev[j]
                else:
                    dp[j + 1] = max(dp[j], prev[j + 1])
            
            prev = dp
        return dp[len(nums2)]