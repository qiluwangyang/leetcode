from typing import List


class Solution:
    @staticmethod
    def subsetsWithDup(nums: List[int]) -> List[List[int]]:
        res = []
        # 重复元素需要排序
        nums.sort()

        def helper(src_lst, temp_lst):
            res.append(temp_lst)
            for i in range(len(src_lst)):
                # 排列顺序后，index为i的元素才会剪枝，不排序时，src_list为[1, 4]时，就不剪枝
                if src_lst[i] in src_lst[:i]:
                    continue
                helper(src_lst[i + 1:], temp_lst + [src_lst[i]])

        helper(nums, [])
        return res


solution = Solution()
print(solution.subsetsWithDup([4, 4, 4, 1, 4]))
