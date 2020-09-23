from typing import List


class Solution:
    @staticmethod
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(index, temp_lst):
            if sum(temp_lst) == target:
                res.append(temp_lst)
                return
            if sum(temp_lst) > target:
                return
            for i in range(index, len(candidates)):
                # 取重复元素，begin从i继续开始
                helper(i, temp_lst + [candidates[i]])

        helper(0, [])
        return res


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
