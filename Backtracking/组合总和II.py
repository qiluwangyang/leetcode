from typing import List


class Solution:
    @staticmethod
    def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(src_lst, tmp_lst):
            if sum(tmp_lst) > target:
                return
            if sum(tmp_lst) == target:
                res.append(tmp_lst)
                return
            for i in range(len(src_lst)):
                if src_lst[i] in src_lst[:i]:
                    continue
                helper(src_lst[i + 1:], tmp_lst + [src_lst[i]])

        helper(candidates, [])
        return res


solution = Solution()
print(solution.combinationSum2([10, 1, 2, 7, 6, 5, 1], 8))
