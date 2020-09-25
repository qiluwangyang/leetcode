from typing import List


class Solution:
    @staticmethod
    def thirdMax(nums: List[int]) -> int:
        # set列表后返回的是set类
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        for i in range(2):
            # 此处使用del比remove耗时少
            del nums[nums.index(max(nums))]
        return max(nums)


solution = Solution()
print(solution.thirdMax([1, 2, 2, 3]))
