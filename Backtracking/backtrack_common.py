from typing import List


class Solution:
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(pos, tmp):
            """
            循环中嵌套循环，当最里层循环结束后方进入下一次循环
            以[1, 2, 3]举例
            第一次循环：helper(1, [1]) -> tmp = []
                第一次循环：helper(2, [1, 2]) -> tmp = [1]
                    第一次循环：helper(3, [1, 2, 3]) -> tmp = [1, 2]
                第二次循环：helper(3, [1, 3]) -> tmp = [1]
            第二次循环：helper(2, [2]) -> tmp = []
                第一次循环：helper(3, [2, 3]) -> tmp = [2]
            第三次循环：helper(3, [3]) -> tmp = []
            """
            res.append(tmp)
            for j in range(pos, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])

        return res
