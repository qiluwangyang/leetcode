from typing import List


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        max1 = count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if max1 < count:
                    max1 = count
                count = 0
        return max(max1, count)


solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
