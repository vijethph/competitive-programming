# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cursum = sum(arr[:k-1])

        for left in range(len(arr) - k + 1):
            cursum += arr[left + k - 1]
            if (cursum / k) >= threshold:
                res += 1
            cursum -= arr[left]
        
        return res
