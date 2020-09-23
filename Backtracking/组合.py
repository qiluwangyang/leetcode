from typing import List


class Solution:
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        """
        :param n: 整数1到n
        :param k: 组合k
        :return: 整型列表
        """
        res = []

        def helper(lst, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(len(lst)):
                helper(lst[i+1:], tmp + [lst[i]])

        helper([ele for ele in range(1, n+1)], [])
        return res


solution = Solution()
print(solution.combine(4, 2))
