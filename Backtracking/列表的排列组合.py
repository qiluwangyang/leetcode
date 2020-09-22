from typing import List


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        """
        :param nums: 整型列表
        :return: 整型列表
        """
        res = []

        def helper(lst, tmp):
            """
            :param lst: 存放原有列表剩余元素
            :param tmp: 存放已经取出的元素的列表
            :return: None
            """
            # 终止条件，当存放原有列表剩余元素为0时，表示所有元素已经加入到tmp列表，此时append到res列表中
            if not lst:
                res.append(tmp)
                return

            for i in range(len(lst)):
                helper(lst[:i] + lst[i + 1:], tmp + [lst[i]])

        helper(nums, [])
        return res


solution = Solution()
print(solution.permute([1, 2, 3]))
