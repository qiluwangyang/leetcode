from typing import List


class Solution:
    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums重新开辟空间，修改参数列表
        # nums[:] = nums[-k:] + nums[:-k]

        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()


outside_nums = [-1, -100, 3, 99]
solution = Solution()
print(solution.rotate(outside_nums, 2))
print(outside_nums)
