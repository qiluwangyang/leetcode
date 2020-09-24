from typing import List


class Solution:
    @staticmethod
    def permutation(s: str) -> List[str]:
        res = []
        s = sorted(s)

        def helper(decrease, increase):
            if not decrease:
                res.append(increase)
                return
            for i in range(len(decrease)):
                if decrease[i] in decrease[:i]:
                    continue
                helper(decrease[:i] + decrease[i+1:], increase+decrease[i])
        helper(s, '')
        return res


solution = Solution()
print(solution.permutation('aab'))
