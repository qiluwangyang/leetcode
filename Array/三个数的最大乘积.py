from typing import List


class Solution:
    @staticmethod
    def maximumProduct(nums: List[int]) -> int:
        nums.sort()
        # 需要考虑前两个数为负数的情况
        return max(nums[-1] * nums[0] * nums[1], nums[-1] * nums[-2] * nums[-3])


solution = Solution()
print(solution.maximumProduct([-3, -2, -1]))
