from typing import List


class Solution:
    @staticmethod
    def sumOddLengthSubarrays(arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1, 2):
                count += sum(arr[i: j])
        return count


solution = Solution()
print(solution.sumOddLengthSubarrays([10, 11, 12]))
