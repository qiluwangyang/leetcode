from typing import List


class Solution:
    @staticmethod
    def permutation(repeat_str: str) -> List[str]:
        res = []

        def helper(decrease_str, increase_str):
            if not decrease_str:
                res.append(increase_str)
            for i in range(len(decrease_str)):
                if decrease_str[i] in decrease_str[:i]:
                    continue
                helper(decrease_str[:i] + decrease_str[i+1:], increase_str + decrease_str[i])
        helper(repeat_str, '')

        return res


solution = Solution()
print(solution.permutation('qqe'))
