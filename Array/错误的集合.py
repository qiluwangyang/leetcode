from typing import List


class Solution:
    @staticmethod
    def findErrorNums(nums: List[int]) -> List[int]:
        # low b 方法
        res = []
        from collections import Counter
        for key, value in Counter(nums).items():
            if value == 2:
                res.append(key)
        for index in range(1, len(nums) + 1):
            if index not in nums:
                res.append(index)
                return res


solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]))
