from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset, result = '', []
        self.DFS(n, subset, result, 0, 0)
        