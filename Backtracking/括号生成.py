from typing import List


class Solution:
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        res = []

        # 定义递归函数
        def helper(left, right, path):
            # 条件在前，然后再递归，否则结果不正确
            # 当右括号大于左括号时，不满足条件，直接退出（剪枝）
            if left < right:
                return
            # 终止条件，当左括号和右括号都都达到上限，将结果存入列表并退出
            if left == n and right == n:
                res.append(path)
                return

            # 左括号加入条件
            if left < n:
                helper(left + 1, right, path + '(')
            # 右括号加入条件
            if right < n:
                helper(left, right + 1, path + ')')

        helper(0, 0, '')
        return res
