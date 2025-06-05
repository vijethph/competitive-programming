# https://leetcode.com/problems/ones-and-zeroes/description/

class Solution:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        dp = defaultdict(int)

        for s in strs:
            mcnt, ncnt = s.count("0"), s.count("1")
            for m in range(M, mcnt - 1, -1):
                for n in range(N, ncnt - 1, -1):
                    dp[(m, n)] = max(1 + dp[(m - mcnt, n - ncnt)], dp[(m, n)])
        
        return dp[(M, N)]