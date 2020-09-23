from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers


solution = Solution()
print(solution.swapNumbers([1, 2]))