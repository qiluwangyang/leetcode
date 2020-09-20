from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [[num] + ele for ele in res]
        return res


solu = Solution()
print(solu.subsets([1, 2, 3]))
