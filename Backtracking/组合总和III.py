from typing import List


class Solution:
    @staticmethod
    def combinationSum3(k: int, n: int) -> List[List[int]]:
        """
        :param k: k个元素
        :param n: 总和为n
        :return: 整型列表
        """
        res = []
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def helper(cur_lst, tmp):
            # 剪枝，当长度超过k时，直接返回
            if len(tmp) > k:
                return
            # 当和为n， 且长度为k时，返回结果
            if sum(tmp) == n and len(tmp) == k:
                res.append(tmp)
                return

            for i in range(len(cur_lst)):
                helper(cur_lst[i + 1:], tmp + [cur_lst[i]])
        helper(lst, [])
        return res


solution = Solution()
print(solution.combinationSum3(3, 9))
