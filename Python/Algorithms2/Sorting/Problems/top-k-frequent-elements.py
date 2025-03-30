# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach 1: sort elements by frequencies and get k most frequent ones - O(nlogn) to sort
        # approach 2: add element frequencies to a max heap where frequency is the key, popping it k times - O(klogn), which includes heapify O(n)
        # approach 3: use bucket sort - O(n) (for both time and space), where the size of bucket is the number of elements in the array
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



